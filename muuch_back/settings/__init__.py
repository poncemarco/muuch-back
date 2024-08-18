import os 
from dotenv import load_dotenv
load_dotenv()
ENVIRONMENT = os.getenv("ENVIRONMENT", "DEVELOPMENT")

if ENVIRONMENT == "DEVELOPMENT":
    from .development import *
elif ENVIRONMENT == "PRODUCTION":
    from .production import *
    
from .base import *