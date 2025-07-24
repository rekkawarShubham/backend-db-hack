import duckdb
import json
from app.models import User
from pydantic.json import pydantic_encoder
from app.utils import deep_merge_dicts  # We'll define this utility


# Connect to DuckDB
con = duckdb.connect("user_data.db")

# Create table with user_id as pk
con.execute("""
CREATE TABLE IF NOT EXISTS user_data (
    user_id INTEGER PRIMARY KEY,
    data JSON
)
""")



def upsert_user(user: User):
    user_id = user.user_id
    conn = duckdb.connect('user_data.db')
    conn.execute("""
                 CREATE TABLE IF NOT EXISTS users
                 (
                     user_id
                     INTEGER
                     PRIMARY
                     KEY,
                     user_json
                     JSON
                 )
                 """)

    # Fetch existing record if exists
    existing = conn.execute("SELECT user_json FROM users WHERE user_id = ?", (user_id,)).fetchone()

    incoming_dict = user.dict(exclude_none=True)

    if existing:
        existing_json = json.loads(existing[0])
        merged_json = deep_merge_dicts(existing_json, incoming_dict)
    else:
        merged_json = incoming_dict

    # Insert/Update with merged JSON
    conn.execute("""
        INSERT OR REPLACE INTO users (user_id, user_json)
        VALUES (?, ?)
    """, (user_id, json.dumps(merged_json, default=pydantic_encoder)))

    conn.close()

def insert_user(user):
    user_dict = user.dict(exclude_none=True)
    user_id = user_dict.get("user_id")

    if user_id is None:
        raise ValueError("user_id is required for insert/update")

    # Delete existing row (if any)
    con.execute("DELETE FROM user_data WHERE user_id = ?", (user_id,))

    # Insert updated row with proper serialization
    con.execute(
        "INSERT INTO user_data (user_id, data) VALUES (?, ?)",
        (user_id, json.dumps(user_dict, default=pydantic_encoder))
    )

def get_user_by_id(user_id: int):
    conn = duckdb.connect('user_data.db')
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            user_json JSON
        )
    """)
    result = conn.execute("SELECT user_json FROM users WHERE user_id = ?", (user_id,)).fetchone()
    conn.close()

    if result:
        return json.loads(result[0])
    return None