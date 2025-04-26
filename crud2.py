from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.errors import ConnectionFailure, PyMongoError


class CRUD:
    def __init__(self, user, password, host, port, db_name, collection_name):
       
        # initializes the CRUD class with MongoDB connection parameters.       
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.db_name = db_name
        self.collection_name = collection_name
        
        #Connect to mongodb
        try:
            self.client = MongoClient(f'mongodb://{self.user}:{self.password}@{self.host}:{self.port}')
            self.database = self.client[self.db_name]
            self.collection = self.database[self.collection_name]
            print(f"onnected to {self.db_name} and {self.collection_name}.")
        except ConnectionFailure as e:
            print(f"error: {e}")
            raise

    def create(self, data):
        
        # inserts a document into the MongoDB collection.
        if data is not None:
            try:
                result = self.collection.insert_one(data)  # insert doc
                return True if result.acknowledged else False
            except PyMongoError as e:
                print(f"error inserting document: {e}")
                return False
        else:
            print("error: data is None")
            return False

    def read(self, query):
        
        # retrieves documents from the MongoDB collection based on query. 
        try:
            cursor = self.collection.find(query)  # find all docs matching the query
            result = list(cursor)  # Convert cursor to a list
            return result if result else []
        except PyMongoError as e:
            print(f"Error querying documents: {e}")
            return [] # return empty list if an error occurs
        
    def update(self, query, new_values):
        
        if query is not None and new_values is not None:
            try:
                result = self.collection.update_one(query, new_values)
                return result.modified_count  
            except PyMongoError as e:
                print(f"Error updating document: {e}")
                return False
        else:
            print("Error: query or new_values is None")
            return False

    def delete(self, query):
        
        if query is not None:
            try:
                result = self.collection.delete_one(query)
                return result.deleted_count 
            except PyMongoError as e:
                print(f"Error deleting document: {e}")
                return False
        else:
            print("Error: query is None")
            return False