#!/usr/bin/python3
"""initialize the models package"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from models.user import User
from models.challenge import Challenge
from models.solution import Solution

classes = {'User': User, 'Challenge': Challenge, 'Solution': Solution}
