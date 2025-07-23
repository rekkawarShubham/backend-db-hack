# app/database.py
import duckdb

conn = duckdb.connect("duckdb.db")

def init_db():
    conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER, name TEXT, age INTEGER, gender TEXT,
        caste TEXT, city TEXT, health_status TEXT, income FLOAT, employment_type TEXT
    )
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS schemes (
        scheme_id INTEGER, name TEXT, category TEXT,
        description TEXT, min_age INT, max_age INT, caste TEXT,
        min_income FLOAT, max_income FLOAT, employment_type TEXT, health_condition TEXT
    )
    """)
