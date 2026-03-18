import sqlite3
import firebase_admin
from firebase_admin import credentials, firestore
import os

def migrate_to_firestore():
    # 1. Initialize Firebase
    json_path = "firebase-adminsdk.json"
    if not os.path.exists(json_path):
        json_path = "backend/firebase-adminsdk.json"
    
    if not os.path.exists(json_path):
        print("Error: firebase-adminsdk.json not found.")
        return

    if not firebase_admin._apps:
        cred = credentials.Certificate(json_path)
        firebase_admin.initialize_app(cred)
    db = firestore.client()

    # 2. Connect to SQLite
    db_path = "backend/schemes.db"
    if not os.path.exists(db_path):
        db_path = "schemes.db"
    
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # --- MIGRATING USERS ---
    print("\n--- Migrating Users ---")
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for u in users:
        u_dict = dict(u)
        uid = str(u_dict['id'])
        # Clean up dict for Firestore
        del u_dict['id']
        db.collection("users").document(uid).set(u_dict, merge=True)
        print(f"Migrated user: {u_dict['email']}")

    # --- MIGRATING SAVED SCHEMES ---
    print("\n--- Migrating Saved Schemes ---")
    cursor.execute("SELECT * FROM saved_schemes")
    saved = cursor.fetchall()
    for s in saved:
        s_dict = dict(s)
        uid = str(s_dict['user_id'])
        scheme_name = s_dict['scheme_name']
        
        # We'll store saved schemes in a subcollection under the user
        db.collection("users").document(uid).collection("saved_schemes").document(scheme_name).set({
            "scheme_name": scheme_name,
            "saved_at": s_dict['saved_at']
        }, merge=True)
        print(f"Migrated saved scheme '{scheme_name}' for user ID {uid}")

    conn.close()
    print("\nFull migration to Firestore complete.")

if __name__ == "__main__":
    migrate_to_firestore()
