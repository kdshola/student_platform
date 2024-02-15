#!/usr/bin/python3
"""
Contains class User for student platform project
"""

from models.base_model import BaseModel, db
from models.solution import Solution
from models.challenge import Challenge
import bcrypt


class User(BaseModel, db.Model):
    """class User for student platform project"""
    __tablename__ = 'user'
    id = db.Column(db.String(64), primary_key=True)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    first_name = db.Column(db.String(64), nullable=True)
    last_name = db.Column(db.String(64), nullable=True)
    profile_picture = db.Column(db.String(256), default='default.jpeg')
    is_suspended = db.Column(db.Boolean, default=False)
    is_instructor = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)
    challenges = db.relationship("Challenge", backref="author",
                                 cascade="all, delete-orphan", lazy=True)
    solutions = db.relationship("Solution", backref="author",
                                cascade="all, delete-orphan", lazy=True)

    def __init__(self, **kwargs):
        """initializes user"""
        super().__init__(**kwargs)
        print(self.password)
        self.set_password(self.password)

    def set_password(self, password):
        """Encrypts user password"""
        salt = bcrypt.gensalt()
        hashpw = bcrypt.hashpw(password.encode('utf8'), salt)
        self.password = hashpw.decode('utf8')

    def check_password(self, password):
        """checks user password for authentication"""
        password = password.encode('utf8')
        return bcrypt.checkpw(password, self.password.encode('utf8'))
