<<<<<<< HEAD
<<<<<<< HEAD
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
=======
#!/usr/bin/python3
"""Database storage engine"""

import os
from sqlalchemy import create_engine
=======
#!/usr/bin/python3
<<<<<<< HEAD
""" new class for sqlAlchemy """
from os import getenv
>>>>>>> 08919b6be8b02f70b773f582199fb593829cd5e8
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
<<<<<<< HEAD

class DBStorage:
    """DBStorage class to interact with MySQL database"""
>>>>>>> 567ab97fa611996363ffe2c98b5736961b62efc4
=======
from models.user import User
=======
"""
Contains the class DBStorage
"""

import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
>>>>>>> 6b99cbf24b82d92f4eae3a673f1d34d96712780e
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
<<<<<<< HEAD
    """ create tables in environmental"""
>>>>>>> 08919b6be8b02f70b773f582199fb593829cd5e8
=======
    """interaacts with the MySQL database"""
>>>>>>> 6b99cbf24b82d92f4eae3a673f1d34d96712780e
    __engine = None
    __session = None

    def __init__(self):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
        """Instantiate the database engine"""
>>>>>>> 567ab97fa611996363ffe2c98b5736961b62efc4
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        database = os.getenv('HBNB_MYSQL_DB')
        
<<<<<<< HEAD
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{database}', pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            self.__drop_all()

    def all(self, cls=None):
        if cls:
            objects = self.__session.query(cls).all()
        else:
            objects = self.__session.query(User, State, City, Amenity, Place, Review).all()
        
        return {f"{type(obj).__name__}.{obj.id}": obj for obj in objects}

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
=======
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
>>>>>>> 567ab97fa611996363ffe2c98b5736961b62efc4
        if obj:
            self.__session.delete(obj)

    def reload(self):
<<<<<<< HEAD
        from models import Base  # Ensure all models are imported
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def __drop_all(self):
        Base.metadata.drop_all(self.__engine)
=======
        """Reload the database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)()

    def close(self):
        """Close the current session"""
        self.__session.close()
>>>>>>> 567ab97fa611996363ffe2c98b5736961b62efc4
=======
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
=======
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
>>>>>>> 6b99cbf24b82d92f4eae3a673f1d34d96712780e
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
<<<<<<< HEAD
        """ calls remove()
        """
        self.__session.close()
>>>>>>> 08919b6be8b02f70b773f582199fb593829cd5e8
=======
        """call remove() method on the private session attribute"""
        self.__session.remove()
>>>>>>> 6b99cbf24b82d92f4eae3a673f1d34d96712780e
