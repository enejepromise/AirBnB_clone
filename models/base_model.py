#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
from copy import deepcopy

class BaseModel:
    """Class that common attributes/method will inherit from"""
    format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *_, **kwargs):
        """Initialize a new BaseModel instance.

    Args:
        *_: Unused positional arguments.
        **kwargs: Keyword arguments for initializing the instance.
            - If kwargs is not empty, the method will set the attributes of the instance
              using the key-value pairs in kwargs, except for the "__class__" key.
            - If kwargs is empty, the method will generate a new unique id and set the
              created_at and updated_at attributes to the current datetime.
    """
        if len(kwargs)!= 0:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        setattr(self,k,datetime.strftime(v,BaseModel.format))
                    else:
                        setattr(self, k,v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = deepcopy(self.created_at)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dct = {}

        dct.update(self.__dict__)
        dct["__class__"] = self.__class__.__name__
        dct["created_at"] = self.created_at.strftime(self.format)
        dct["updated_at"] = self.updated_at.strftime(self.format)

        return dct

    def __str__(self) -> str:
        return f"[{self.__class__. __name__}] ({self.id}) {self.__dict__}"

