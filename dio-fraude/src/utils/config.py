import os 
from dotenv import load_dotenv
load_dotenv()

class config:
    ENDPOINT =  os.getenv("ENDPOINT")
    KEY = os.getenv("key")
    STORAGE_CONNECTION_STRING = os.getenv("STORAGE-CONNECTION-STRING")
    CONTAINER_NAME = os.getenv("CONTAINER-NAME")