from datetime import datetime, timezone
from fastapi import HTTPException
from database import db_instance
from pymongo.errors import ConnectionFailure, OperationFailure, PyMongoError
from utils import DatabaseError, NotFoundError

class UserDAO:

    
    def __init__(self):
        try:
            self.user_collection = db_instance.get_collection("users_collection")
        except ConnectionFailure as connection_failure:
            print("Unable to connect to user_collection", connection_failure)
            self.user_collection = None
            raise DatabaseError("Unable to connect to user_collection", 500) from connection_failure

    
    def find_user_by_email(self, email: str):
        try:
            existing_user = self.user_collection.find_one({"email": email})
            return existing_user
        except OperationFailure as operation_failure:
            raise DatabaseError("Failed to fetch user from database.", 500) from operation_failure
    
    
    def update_existing_user_last_login(self, email: str):
        try:
            self.users_collection.update_one({"email": email}, {"$set": {"last_login": datetime.now(timezone.utc()).isoformat()}})
        except OperationFailure as operation_failure:
            raise DatabaseError("Couldn't update user's last login.", 500) from operation_failure
        
        
    def create_user(self, user_data: dict):
        try:
            user_data.created_at = datetime.now(timezone.utc).isoformat()
            user_data.last_login = datetime.now(timezone.utc).isoformat()
            result = self.user_collection.insert_one(user_data.model_dump())
            return str(result.inserted_id)
        except PyMongoError as error:
            print("Error creating user: ", error)
            raise HTTPException(status_code=500, detail={"message": "Error creating user"})
        