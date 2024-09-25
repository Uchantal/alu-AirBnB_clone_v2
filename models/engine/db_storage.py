#!/usr/bin/python3
"""Database storage engine"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City

class DBStorage:
    """DBStorage class to interact with MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate the database engine"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        database = os.getenv('HBNB_MYSQL_DB')
        
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'.format(user, password, host, database), pool_pre_ping=True)
        
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects by class name or all objects"""
        obj_dict = {}
        if cls:
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = f"{obj.__class__.__name__}.{obj.id}"
                obj_dict[key] = obj
        else:
            for cls_name in [State, City]:
                objects = self.__session.query(cls_name).all()
                for obj in objects:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """Add the object to the session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes in the session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload the database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)()

    def close(self):
        """Close the current session"""
        self.__session.close()
