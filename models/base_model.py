#!/usr/bin/python3
import uuid
from datetime import datetime
import models

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{:s}] ({:s}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        new = dict(self.__dict__)
        new["__class__"] = type(self).__name__
        new["created_at"] = new["created_at"].isoformat()
        new["updated_at"] = new["updated_at"].isoformat()

        return new


