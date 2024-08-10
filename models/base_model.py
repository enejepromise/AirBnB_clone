#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from uuid import uuid4
from datetime import datetime

class BaseModel(self):
    """This is a basemodel that defines all the instances of a common element"""
    def __ini__(self):
        self.id = str(uuid4)
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
   
   def __str__(self):
        """Return a string representation of the instance."""
        return f"[{self.__class__. __name__}] (self.id) {self.__dict__}"
    
    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.utcnow()
    
    def to_dict(self):
        """Return a dictionary representation of the instance."""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = [self.__class__.__name__]
        my_dict["self.created_at"] = datetime.utcnow()
        my_dict["self.updated_at"] = datetime.utcnow()
        return my_dict
