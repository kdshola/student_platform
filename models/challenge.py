#!/usr/bin/python3
"""
Contains class Challenge for student platform project
"""

from models.base_model import BaseModel, db


class Challenge(BaseModel, db.Model):
    """class Challenge for student platform project"""
    __tablename__ = 'challenge'
    id = db.Column(db.String(60), primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    verified = db.Column(db.Boolean, default=False)
    topic = db.Column(db.String(128), nullable=False)
    image = db.Column(db.String(256), nullable=True)
    user_id = db.Column(db.String(60), db.ForeignKey('user.id'),
                        nullable=False)

    def __init__(self, **kwargs):
        """initializes challenge"""
        super().__init__(**kwargs)
