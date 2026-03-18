import pandas as pd
import sqlite3

# Load Excel file
df = pd.read_excel("NSP_Scholarships_FINAL_STANDARDIZED.xlsx")

# Connect to SQLite database
conn = sqlite3.connect("schemes.db")

# Store data into table
df.to_sql("central_schemes", conn, if_exists="replace", index=False)

conn.close()

print("✅ Database created successfully!")