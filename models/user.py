#!/usr/bin/python3

from base_model import BaseModel

class user(BaseModel):
    email: ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""


def __init__(self, *args, **kwargs):
        """initialization of user objects"""
        super().__init__(*args, **kwargs)
