import sqlite3
import os

def migrate_users_table():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "schemes.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Columns to add
    new_columns = [
        ("dob", "TEXT"),
        ("gender", "TEXT"),
        ("category", "TEXT"),
        ("income", "INTEGER"),
        ("education", "TEXT"),
        ("employment_status", "TEXT"),
        ("state_residence", "TEXT"),
        ("university", "TEXT"),
        ("address", "TEXT"),
        ("profile_complete", "INTEGER DEFAULT 0")
    ]

    for col_name, col_type in new_columns:
        try:
            cursor.execute(f"ALTER TABLE users ADD COLUMN {col_name} {col_type}")
            print(f"Added column: {col_name}")
        except sqlite3.OperationalError:
            print(f"Column already exists: {col_name}")

    conn.commit()
    conn.close()
    print("User table migration complete.")

if __name__ == "__main__":
    migrate_users_table()
