import sqlite3

# Sample user input (we'll make this dynamic later)
user = {
    "age": 17,
    "income": 200000,
    "category": "SC",
    "gender": "All",
    "education_level": "Class 10"
}

conn = sqlite3.connect("schemes.db")
cursor = conn.cursor()

query = """
SELECT scheme_name, education_level, gender
FROM central_schemes
WHERE
    min_age <= ?
    AND max_age >= ?
    AND max_income >= ?
    AND (category = ? OR category = 'All')
"""

cursor.execute(query, (
    user["age"],
    user["age"],
    user["income"],
    user["category"]
))


results = cursor.fetchall()

print("Eligible Schemes:\n")
for scheme in results:
    print(scheme[0])

conn.close()