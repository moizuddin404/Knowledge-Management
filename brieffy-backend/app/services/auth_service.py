from datetime import datetime
from database import db_instance
from models import User
from config import Config
import jwt


class AuthService:
    def __init__(self):
        self.users_collection = db_instance.get_collection("users_collection")

    def authenticate_user(self, user_data: User):
        existing_user = self.users_collection.find_one({"email": user_data.email})

        if existing_user:
            self.users_collection.update_one({"email": user_data.email}, {"$set": {"last_login": datetime.utcnow().isoformat()}}
                                             )
            status = "existing"
        
        else:
            user_data.created_at = datetime.utcnow().isoformat()
            user_data.last_login = datetime.utcnow().isoformat()
            self.users_collection.insert_one(user_data.dict())

            status = "new"
        
        token_payload = {"email": user_data.email}
        token = jwt.encode(token_payload, Config.SECRET_KEY, algorithm="HS256")

        return{"message": f"User {status}", "token": token}
        
