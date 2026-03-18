import sqlite3
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, "schemes.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# USERS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT DEFAULT 'user'
)
""")

# SAVED SCHEMES TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS saved_schemes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    scheme_name TEXT,
    saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")

conn.commit()
conn.close()

print("✅ Auth tables created successfully!")