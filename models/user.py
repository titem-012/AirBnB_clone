#!/usr/bin/python3
"""
this is the users class inheriting the parent class Basemodel
"""
from models.base_model import BaseModel
class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
