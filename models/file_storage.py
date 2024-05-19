#!/usr/bin/python3
'''AirBnB clone project File Storage'''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
from models.state import State


class FileStorage:
    """ This is my storage engine for the AirBnB clone project
        all: Returns the object
        new: makes and update the dictionary id
        save: Serializes, or converts Python objects into JSON strings
        reload: converts JSON strings into Python objects.
    Class Attributes:
        __file_path (str): The file name to save objects to.
        __objects (dict): the dictionary for my objects.
        class_dict (dict): A dictionary for all the classes present.
    """

    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}

    def all(self):
        '''Return dictionary of <class>.<id> : object instance'''
        return self.__objects

    def new(self, obj):
        '''Set new __objects to existing dictionary of instances'''
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Saves object dictionaries to the  json file"""
        obj_dict = {}
                                                          1,16
