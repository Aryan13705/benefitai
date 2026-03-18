import firebase_admin
from firebase_admin import credentials, firestore
import os

def test_connection():
    try:
        if os.path.exists("firebase-adminsdk.json"):
            print("Found firebase-adminsdk.json")
            cred = credentials.Certificate("firebase-adminsdk.json")
            firebase_admin.initialize_app(cred)
            db = firestore.client()
            # Try to fetch a single document from schemes
            docs = db.collection("schemes").limit(1).get()
            print(f"Successfully connected! Found {len(docs)} schemes.")
        else:
            print("firebase-adminsdk.json NOT FOUND")
    except Exception as e:
        print(f"Connection FAILED: {e}")

if __name__ == "__main__":
    test_connection()
