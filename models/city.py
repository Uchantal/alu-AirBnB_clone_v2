#!/usr/bin/python3
<<<<<<< HEAD
""" City Module for HBNB project """
<<<<<<< HEAD
from models.base_model import BaseModel
=======
"""City module"""
>>>>>>> 567ab97fa611996363ffe2c98b5736961b62efc4
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
=======
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
>>>>>>> 08919b6be8b02f70b773f582199fb593829cd5e8

class City(BaseModel, Base):
<<<<<<< HEAD
    __tablename__ = 'cities'

<<<<<<< HEAD
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    state = relationship("State", back_populates="cities")
=======
    """The City class, contains state ID and name"""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
>>>>>>> 567ab97fa611996363ffe2c98b5736961b62efc4
=======
class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = 'cities'

    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities")
>>>>>>> 08919b6be8b02f70b773f582199fb593829cd5e8
