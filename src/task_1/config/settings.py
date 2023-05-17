import os
from dotenv import load_dotenv


load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@127.0.0.1:5434/{DB_NAME}'
