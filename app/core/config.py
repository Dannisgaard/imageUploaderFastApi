import os
from dotenv import load_dotenv
from starlette.datastructures import CommaSeparatedStrings, Secret
from databases import DatabaseURL

API_V1_STR = "/api"

JWT_TOKEN_PREFIX = "Token"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # one week

load_dotenv(verbose=True)

MAX_CONNECTIONS_COUNT = int(os.getenv("MAX_CONNECTIONS_COUNT", 10))
MIN_CONNECTIONS_COUNT = int(os.getenv("MIN_CONNECTIONS_COUNT", 10))
SECRET_KEY = Secret(os.getenv("SECRET_KEY", "secret key for project"))

PROJECT_NAME = os.getenv("PROJECT_NAME", "FastAPI rygmoede api")
ALLOWED_HOSTS = str(os.getenv("ALLOWED_HOSTS"))

MONGODB_URL = os.getenv("MONGODB_URL", "")
MONGO_DB = os.getenv("MONGO_DB", "rygmoede")
if not MONGODB_URL:
    MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
    MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
    MONGO_USER = os.getenv("MONGO_USER", "superuser")
    MONGO_PASS = os.getenv("MONGO_PASSWORD", "changeMeToAStrongPassword")

    MONGODB_URL = DatabaseURL(
        f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
    )
else:
    MONGODB_URL = DatabaseURL(MONGODB_URL)

database_name = MONGO_DB
mettings_collection_name = "mettings"
tags_collection_name = "tags"
persons_collection_name = "persons"
photos_collection_name = "photos"
users_collection_name = "users"
meetings_collection_name = "meetings"