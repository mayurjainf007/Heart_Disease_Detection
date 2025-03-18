import psycopg2
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB", "heart_disease"),
            user=os.getenv("POSTGRES_USER", "admin"),
            password=os.getenv("POSTGRES_PASSWORD", "password"),
            host=os.getenv("DB_HOST", "db"),
            port=os.getenv("DB_PORT", "5432")
        )
        logging.info("Database connection established successfully")
        return conn
    except Exception as e:
        logging.error(f"Error connecting to database: {str(e)}")
        return None
