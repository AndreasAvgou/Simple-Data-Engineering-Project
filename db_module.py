import logging
import psycopg2
import os

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "user")
DB_PASS = os.getenv("DB_PASS", "password")
DB_NAME = os.getenv("DB_NAME", "coffee_db")

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        dbname=DB_NAME
    )

def init_db():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS coffee_data (
                id SERIAL PRIMARY KEY,
                title TEXT,
                description TEXT,
                desc_length INTEGER,
                ingredient_count INTEGER
            );
        ''')
        conn.commit()
        conn.close()
        logging.info("PostgreSQL database initialized.")
    except Exception as e:
        logging.error(f"PostgreSQL init error: {e}")

def insert_data(df):
    try:
        conn = get_connection()
        cur = conn.cursor()
        for _, row in df.iterrows():
            cur.execute('''
                INSERT INTO coffee_data (title, description, desc_length, ingredient_count)
                VALUES (%s, %s, %s, %s)
            ''', (
                row.get('title', ''),
                row.get('description', ''),
                row.get('desc_length', 0),
                row.get('ingredient_count', 0)
            ))
        conn.commit()
        conn.close()
        logging.info("Data inserted into PostgreSQL.")
    except Exception as e:
        logging.error(f"PostgreSQL insert error: {e}")
