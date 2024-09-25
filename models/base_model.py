#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import models

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if kwargs:
            # Remove __class__ if present
            kwargs.pop('__class__', None)
            # Parse datetime strings back to datetime objects
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
            # Generate id if not present
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            # Set created_at and updated_at if not present
            if 'created_at' not in kwargs:
                self.created_at = datetime.utcnow()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.utcnow()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls_name = self.__class__.__name__
        return '[{}] ({}) {}'.format(cls_name, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)  # Moved from __init__ to here
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        my_dict = dict(self.__dict__)
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        # Remove _sa_instance_state if it exists
        my_dict.pop('_sa_instance_state', None)
        return my_dict

    def delete(self):
        """Deletes the current instance from the storage"""
        models.storage.delete(self)
