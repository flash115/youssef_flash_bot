import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY,
            email TEXT,
            token TEXT,
            created_at TEXT
        )
        """)
        self.conn.commit()

    def add_user(self, user_id):
        self.cursor.execute(
            "INSERT OR IGNORE INTO users(user_id) VALUES(?)",
            (user_id,)
        )
        self.conn.commit()

    def set_email(self, user_id, email, token):
        self.cursor.execute(
            "UPDATE users SET email=?, token=? WHERE user_id=?",
            (email, token, user_id)
        )
        self.conn.commit()

    def get_user(self, user_id):
        self.cursor.execute(
            "SELECT * FROM users WHERE user_id=?",
            (user_id,)
        )
        return self.cursor.fetchone()
