#!/usr/bin/python3
"""A code containging the Basemodel on the created at, updated_at"""
import datetime
import uuid
class BaseModel:
    def __init__(self, *args, **kwargs):
        """making a public instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()
    def __str__(self):
        """The Function that  returns the string representation of the instance"""
        return "[{}] ({}) {}.format(self.__class__.__name__, self.id, self.__dict__)"
    def save(self):
        """The function updates the updated time"""
        self.updated_at = datetime.datetime.utcnow().isoformat()
    def to_dict(self):
        instance_dict = self.__dict__copy()
        instance_dict["__class__"] = self.__class__.name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instancce_dict["updated_at"] = self.updated_at.isorformat()
        return instance_dict
