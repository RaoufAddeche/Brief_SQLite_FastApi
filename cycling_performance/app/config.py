import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Environment variables
SECRET_KEY = os.getenv("SECRET_KEY")  # Secret key for signing JWT tokens
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")  # Token expiration time in minutes
DATABASE_URL = os.getenv("DATABASE_URL")  # URL for the SQLite database
ALGORITHM = os.getenv("ALGORITHM")  # Algorithm used for JWT encoding/decoding