#!/usr/bin/python3
<<<<<<< HEAD
<<<<<<< HEAD
"""This module instantiates an object of class FileStorage"""
import os

<<<<<<< HEAD
if os.getenv('HBNB_TYPE_STORAGE') == 'db':
=======
"""Initialization of models package"""
from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
>>>>>>> 567ab97fa611996363ffe2c98b5736961b62efc4
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()

=======
if os.getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
=======
"""
initialize the models package
"""

from os import getenv


storage_t = getenv("HBNB_TYPE_STORAGE")
>>>>>>> 6b99cbf24b82d92f4eae3a673f1d34d96712780e

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
<<<<<<< HEAD
    storage.reload()
>>>>>>> 08919b6be8b02f70b773f582199fb593829cd5e8
=======
storage.reload()
>>>>>>> 6b99cbf24b82d92f4eae3a673f1d34d96712780e
