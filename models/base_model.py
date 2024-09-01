#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
from copy import deepcopy

class BaseModel:
    """Class that will common attributes/method will inherit from"""
    format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self):
        """This a method that initailizes"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = deepcopy(self.created_at)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dct = {}
        dct.update(self.__dict__)
        dct["__class__"] = self.__class__.__name__
        dct["created_at"] = self.datetime.strftime(self.format)
        dct["updated_at"] = self.datetime.strftime(self.format)

        return dct

    def __str__(self) -> str:
        return f"[{self.__class__. __name__}] ({self.id}) {self.__dict__}"

