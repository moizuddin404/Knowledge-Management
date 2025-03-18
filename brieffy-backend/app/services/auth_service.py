from datetime import datetime
from database import db_instance
from models import User
from config import Config
from utils import create_access_token, decode_access_token


class AuthService:
    def __init__(self):
        self.users_collection = db_instance.get_collection("users_collection")

    def authenticate_user(self, user_data: User):
        existing_user = self.users_collection.find_one({"email": user_data.email})

        if existing_user:
            self.users_collection.update_one({"email": user_data.email}, {"$set": {"last_login": datetime.utcnow().isoformat()}}
                                             )
            user_id = str(existing_user["_id"])
           
            status = "existing"
        
        else:
            user_data.created_at = datetime.utcnow().isoformat()
            user_data.last_login = datetime.utcnow().isoformat()
            result = self.users_collection.insert_one(user_data.dict())

            user_id = str(result.inserted_id)

            status = "new"
        
        token_payload = {"userId": user_id,"email": user_data.email}
        token = create_access_token(token_payload)

        return{"message": f"User {status}", "token": token}
        
