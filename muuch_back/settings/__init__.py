import os 
from dotenv import load_dotenv
load_dotenv()
ENVIRONMENT = os.getenv("ENVIROMENT", "DEVELOPMENT")
print(os.getenv("ENVIROMENT"))
if ENVIRONMENT == "DEVELOPMENT":
    from .development import *
elif ENVIRONMENT == "PRODUCTION":
    print(os.getenv("ENVIROMENT"))
    from .production import *
    
from .base import *