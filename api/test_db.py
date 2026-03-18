import sqlite3

conn = sqlite3.connect("schemes.db")
cursor = conn.cursor()

cursor.execute("SELECT scheme_name, max_income FROM central_schemes LIMIT 5")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()