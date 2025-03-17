import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLLIENT_ID")
    SECRET_KEY = os.getenv("SECRET_KEY")