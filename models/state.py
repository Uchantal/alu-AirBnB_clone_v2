#!/usr/bin/python3
<<<<<<< HEAD
<<<<<<< HEAD
""" State Module for HBNB project """
<<<<<<< HEAD
=======
"""State module"""
>>>>>>> 567ab97fa611996363ffe2c98b5736961b62efc4
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
=======
=======
""" holds class State"""
>>>>>>> 6b99cbf24b82d92f4eae3a673f1d34d96712780e
import models
from models.base_model import BaseModel, Base
from models.city import City
<<<<<<< HEAD
>>>>>>> 08919b6be8b02f70b773f582199fb593829cd5e8

class State(BaseModel, Base):
<<<<<<< HEAD
    __tablename__ = 'states'

<<<<<<< HEAD
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state", cascade="all, delete-orphan")
=======
    """State class"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
=======
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
>>>>>>> 6b99cbf24b82d92f4eae3a673f1d34d96712780e

    # Relationship with City; cascade delete
    cities = relationship('City', backref='state', cascade='all, delete-orphan')

    @property
    def cities(self):
        """Getter for FileStorage to return related cities"""
        from models import storage
        city_list = []
        for city in storage.all('City').values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
>>>>>>> 567ab97fa611996363ffe2c98b5736961b62efc4
=======
class State(BaseModel, Base):
    """Representation of state """
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def cities(self):
<<<<<<< HEAD
            """ Returns the list of City instances with state_id
            equals to the current State.id. """
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
>>>>>>> 08919b6be8b02f70b773f582199fb593829cd5e8
=======
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
>>>>>>> 6b99cbf24b82d92f4eae3a673f1d34d96712780e
