#!/usr/bin/python3
<<<<<<< HEAD
""" City Module for HBNB project """
from models.base_model import BaseModel
=======
"""City module"""
>>>>>>> 567ab97fa611996363ffe2c98b5736961b62efc4
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class City(BaseModel, Base):
<<<<<<< HEAD
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    state = relationship("State", back_populates="cities")
=======
    """The City class, contains state ID and name"""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
>>>>>>> 567ab97fa611996363ffe2c98b5736961b62efc4
