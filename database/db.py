import sqlite3

DB_NAME = "database.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY,
        email TEXT,
        token TEXT,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()
