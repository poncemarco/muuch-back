DEBUG = True
from .base import BASE_DIR
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

DATABASES = {
        'default' : {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv('DB_NAME'),
            "USER": os.getenv('DB_USER'),
            "PASSWORD": os.getenv('DB_PASSWORD'),
            "HOST": "localhost",
            "PORT": "5432",
        }
    }