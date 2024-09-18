DEBUG = True
from .base import BASE_DIR
from dotenv import load_dotenv
import os

load_dotenv()

DATABASES = {
        'default' : {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "muuch",
            "USER": os.getenv('DB_USER'),
            "PASSWORD": os.getenv('DB_PASSWORD'),
            "HOST": "localhost",
            "PORT": "",
        }
    }