#!/usr/bin/python3
<<<<<<< HEAD
""" State Module for HBNB project """
=======
"""State module"""
>>>>>>> 567ab97fa611996363ffe2c98b5736961b62efc4
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class State(BaseModel, Base):
<<<<<<< HEAD
    __tablename__ = 'states'

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
