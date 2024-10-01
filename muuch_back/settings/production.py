from dotenv import load_dotenv
import os

load_dotenv()

DEBUG = False

SECRET_KEY = os.getenv('SECRET_KEY')
print(os.getenv("ENVIROMENT"))

DATABASES = {
        'default' : {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv('DB_NAME'),
            "USER": os.getenv('DB_USER'),
            "PASSWORD": os.getenv('DB_PASSWORD'),
            "HOST": "db",
            "PORT": "5432",
        }
    }