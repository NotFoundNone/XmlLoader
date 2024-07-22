import psycopg2
import os
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), 'local.env')

load_dotenv(dotenv_path=env_path)

DB_NAME = os.getenv('DB_NAME', 'postgres')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DATA_DIR = os.getenv('DATA_DIR', 'files')


def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            options='-c client_encoding=UTF8'
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        raise
