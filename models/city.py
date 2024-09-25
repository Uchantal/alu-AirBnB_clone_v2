<<<<<<< HEAD
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
=======
#!/usr/bin/python
""" holds class City"""
import models
>>>>>>> 6b99cbf24b82d92f4eae3a673f1d34d96712780e
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
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
    """Representation of city """
    if models.storage_t == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""

<<<<<<< HEAD
    __tablename__ = 'cities'

    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities")
>>>>>>> 08919b6be8b02f70b773f582199fb593829cd5e8
=======
    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
>>>>>>> 6b99cbf24b82d92f4eae3a673f1d34d96712780e
