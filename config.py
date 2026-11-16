



import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    
    
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-me")

    
    
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "postgresql+psycopg2://postgres:postgres@localhost:5432/my_app_db",
    )

    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
