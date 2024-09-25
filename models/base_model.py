#!/usr/bin/python3
<<<<<<< HEAD
<<<<<<< HEAD
"""This module defines a base class for all models in our hbnb clone"""

=======
"""This is the base model class for AirBnB"""
=======
"""
Contains class BaseModel
"""

from datetime import datetime
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime
>>>>>>> 6b99cbf24b82d92f4eae3a673f1d34d96712780e
from sqlalchemy.ext.declarative import declarative_base
>>>>>>> 08919b6be8b02f70b773f582199fb593829cd5e8
import uuid
<<<<<<< HEAD
import models
from datetime import datetime
<<<<<<< HEAD
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import models
=======
from sqlalchemy import Column, Integer, String, DateTime
=======
>>>>>>> 6b99cbf24b82d92f4eae3a673f1d34d96712780e

time = "%Y-%m-%dT%H:%M:%S.%f"

<<<<<<< HEAD
Base = declarative_base()
>>>>>>> 08919b6be8b02f70b773f582199fb593829cd5e8
=======
if models.storage_t == "db":
    Base = declarative_base()
else:
    Base = object
>>>>>>> 6b99cbf24b82d92f4eae3a673f1d34d96712780e

Base = declarative_base()

class BaseModel:
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
    """This class will defines all common attributes/methods
    for other classes
    """
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
=======
    """The BaseModel class from which future classes will be derived"""
    if models.storage_t == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)
>>>>>>> 6b99cbf24b82d92f4eae3a673f1d34d96712780e

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

    def delete(self):
<<<<<<< HEAD
        """ delete object
        """
        models.storage.delete(self)
>>>>>>> 08919b6be8b02f70b773f582199fb593829cd5e8
=======
        """delete the current instance from the storage"""
        models.storage.delete(self)
>>>>>>> 6b99cbf24b82d92f4eae3a673f1d34d96712780e
