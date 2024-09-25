import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        database = os.getenv('HBNB_MYSQL_DB')
        
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
        if obj:
            self.__session.delete(obj)

    def reload(self):
        from models import Base  # Ensure all models are imported
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def __drop_all(self):
        Base.metadata.drop_all(self.__engine)
