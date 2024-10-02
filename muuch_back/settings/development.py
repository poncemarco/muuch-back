DEBUG = True
from .base import BASE_DIR
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

USE_S3 = True

# AWS settings
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_DEFAULT_ACL = None
AWS_S3_REGION_NAME = 'us-east-2'
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_S3_SIGNATURE_VERSION = 's3v4'

# S3 static settings
STATIC_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
STATICFILES_STORAGE = 'muuch_back.storages.StaticStorage'

# S3 public media settings
PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = 'muuch_back.storages.StaticStorage.PublicMediaStorage'
THUMBNAIL_DEFAULT_STORAGE = 'muuch_back.storages.StaticStorage.PublicMediaStorage'

# S3 private media settings
PRIVATE_MEDIA_LOCATION = 'private'
PRIVATE_FILE_STORAGE = 'muuch_back.storages.StaticStorage.PrivateMediaStorage'    

# Static files directories
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), os.path.join(BASE_DIR, 'media'))

# Define STATIC_ROOT
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_temp')

# Database settings
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv('DB_NAME'),
        "USER": os.getenv('DB_USER'),
        "PASSWORD": os.getenv('DB_PASSWORD'),
        "HOST": "localhost",
        "PORT": "5432",
    }
}
