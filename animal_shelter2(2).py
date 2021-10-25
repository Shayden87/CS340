from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
from bson import json_util, ObjectId
import json


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:37211/AAC' % (username, password))
        self.database = self.client['AAC']

# Implements the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)
            return True      
        else:
            return False

# Implements the R in CRUD.
    def read(self, inquiry):
        if inquiry is not None:
            result = self.database.animals.find(inquiry,{"_id":False})
            return result
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Implements the U in CRUD.
    def update(self, inquiry, newValue):
        if inquiry is not None:
            result = self.database.animals.update_one(inquiry, newValue)
            doc = self.database.animals.find_one(inquiry)
            print(doc)
        else:
            raise Exception("Update not successful")
            
# Implements the D in CRUD.
    def delete(self, inquiry):
        if inquiry is not None:
            result = self.database.animals.delete_one(inquiry)
            print(result)
            for x in self.database.animals.find():
                print(x)
        else:
            raise Exception("Delete not successful")
