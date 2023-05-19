import os
from dotenv import load_dotenv


load_dotenv()

DB_NAME = os.getenv('POSTGRES_DB')
DB_USER = os.getenv('POSTGRES_USER')
DB_PASS = os.getenv('POSTGRES_PASSWORD')
DB_PORT = os.getenv('POSTGRES_PORT')

DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@127.0.0.1:5434/{DB_NAME}'
