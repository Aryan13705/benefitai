import sqlite3

conn = sqlite3.connect("schemes.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM central_schemes")
print("Total rows:", cursor.fetchone()[0])

conn.close()
