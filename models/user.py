#!/usr/bin/python3
"""This module defines a class User"""
from uuid import uuid4
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models import hbnb_storage
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship(
        'Place',
        backref='user_relationship',
        cascade='all, delete, delete-orphan',
        single_parent=True
    )

    reviews = relationship(
        'Review',
        backref='user_relationship',
        cascade='all, delete, delete-orphan',
        single_parent=True
    )
