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
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """ create tables in environmental"""
>>>>>>> 08919b6be8b02f70b773f582199fb593829cd5e8
    __engine = None
    __session = None

    def __init__(self):
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
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            lista = [State, City, User, Place, Review, Amenity]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)

    def new(self, obj):
        """add a new element in the table
        """
        self.__session.add(obj)

    def save(self):
        """save changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete an element in the table
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """configuration
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """ calls remove()
        """
        self.__session.close()
>>>>>>> 08919b6be8b02f70b773f582199fb593829cd5e8
