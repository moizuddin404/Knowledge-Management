from pymongo import MongoClient
from config import Config

class Database:
    def __init__(self):
        self.client = MongoClient(Config.MONGO_URI)
        self.db = self.client["brieffydb"]
        self.users_collection = self.db["users_collection"]

    def get_collection(self, collection_name):
        return self.db[collection_name]
    