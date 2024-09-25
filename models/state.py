#!/usr/bin/python3
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
import models
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
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
    """ State class """

    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        @property
        def cities(self):
            """ Returns the list of City instances with state_id
            equals to the current State.id. """
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
>>>>>>> 08919b6be8b02f70b773f582199fb593829cd5e8
