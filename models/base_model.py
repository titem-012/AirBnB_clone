#!/usr/bin/python3
"""A code containging the Basemodel on the created at, updated_at"""
import models
import datetime
import uuid
class BaseModel():
    """This is the root projects Class to be inherited"""
    classes = {}
    def __init__(self, *args, **kwargs):
        """making a public instance"""
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                    setattr(self, key, value)
            return

            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.utcnow().isoformat()
            
            storage.new(self)
            super().__init__(*args, **kwargs)

    def __str__(self):
        """The Function that  returns the string representation of the instance"""
        return "[{}] ({}) {}.format(self.__class__.__name__, self.id, self.__dict__)"

    def save(self):
        """The function updates the updated time"""
        self.updated_at = datetime.datetime.utcnow().isoformat()
        storage.save()

    def to_dict(self):
        """Dictionary to the instances"""
        instance_dict = {**self.__dict__}
        instance_dict["__class__"] = type(self).__name__
        instance_dict['created_at'] = self.created_at

        if hasattr(instance_dict['updated_at']):
            instance_dict['updated_at'] =self.updated_at

        return instance_dict
