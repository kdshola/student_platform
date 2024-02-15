#!/usr/bin/python3
"""
Contains class BaseModel for student platform project
"""

from models import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """The Base class for classes in student platform project"""
    id = db.Column(db.String(60), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, **kwargs):
        """Initializes an instance of a base model
        Args:
             self: an instance of a base model or its subclass
             kwargs (dict): key value pairs of instance attribute
        Returns:
             BaseModel: An instance of base model class
        """
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
            if 'created_at' not in kwargs:
                self.created_at = datetime.utcnow()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.utcnow()
        else:
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        self.id = str(uuid.uuid4())

    def __str__(self):
        """String representation of the BaseModel class"""
        return f"{self.__class__.__name__}: {self.id}, {self.__dict__}"

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance
        """
        copy = dict(self.__dict__)
        if "_sa_instance_state" in copy:
            del copy["_sa_instance_state"]
        copy["__class__"] = self.__class__.__name__
        if "updated_at" in copy:
            copy["updated_at"] = copy["updated_at"].strftime(time_format)
        if "created_at" in copy:
            copy["created_at"] = copy["created_at"].strftime(time_format)
        if str(type(self)) == 'User':
            del copy["password"]
            if "is_instructor" in copy:
                del copy["is_instructor"]
            if "is_admin" in copy:
                del copy["is_admin"]
            if "profile_picture" in copy:
                del copy["profile_picture"]

        if "verified" in copy:
            del copy["verified"]
        if "image" in copy:
            del copy["image"]
        return copy
