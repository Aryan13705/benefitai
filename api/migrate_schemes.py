import sqlite3
import firebase_admin
from firebase_admin import credentials, firestore
import os

def migrate():
    # 1. Initialize Firebase
    json_path = "firebase-adminsdk.json"
    if not os.path.exists(json_path):
        json_path = "../firebase-adminsdk.json"
    
    if not os.path.exists(json_path):
        print("Error: firebase-adminsdk.json not found in current or parent directory.")
        return

    cred = credentials.Certificate(json_path)
    try:
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        print("Connected to Firestore.")
    except Exception as e:
        print(f"Failed to connect to Firestore: {e}")
        return

    # 2. Connect to SQLite
    db_path = "schemes.db"
    if not os.path.exists(db_path):
        print(f"Error: {db_path} not found.")
        return

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # 3. Fetch all opportunities
    cursor.execute("SELECT * FROM opportunities")
    rows = cursor.fetchall()
    print(f"Found {len(rows)} schemes in SQLite.")

    # 4. Migrate to Firestore
    collection_name = "schemes"
    count = 0
    for row in rows:
        data = dict(row)
        # Convert row to dict and remove SQLite specific 'id' if you want Firestore to generate one, 
        # or use it as document ID. Let's use it as document ID for consistency.
        doc_id = str(data['id'])
        
        try:
            db.collection(collection_name).document(doc_id).set(data)
            count += 1
            print(f"Migrated: {data['name']} (ID: {doc_id})")
        except Exception as e:
            print(f"Failed to migrate {data['id']}: {e}")

    print(f"Successfully migrated {count} schemes to Firestore collection '{collection_name}'.")
    conn.close()

if __name__ == "__main__":
    migrate()
