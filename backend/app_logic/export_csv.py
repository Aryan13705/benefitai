import sqlite3
import csv
import sys
import os

# Add current directory to path so we can import institutes_data
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from institutes_data import INSTITUTES_DATA, NATIONAL_ENTRANCE_EXAMS

def export_sqlite_to_csv():
    try:
        conn = sqlite3.connect("database.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM opportunities")
        rows = cursor.fetchall()
        
        if rows:
            with open("schemes_data.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(rows[0].keys())
                for row in rows:
                    writer.writerow(row)
            print("✅ Exported SQLite opportunities to schemes_data.csv")
    except Exception as e:
        print(f"❌ Error exporting SQLite data: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

def export_institutes_to_csv():
    try:
        with open("institutes_data.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            # Headers
            writer.writerow(["State", "Name", "Type", "Location", "Category", "Established", "Ranking", "Website", "Entrance Exams"])
            
            for state, institutes in INSTITUTES_DATA.items():
                for i in institutes:
                    exams = ", ".join(i.get("entrance_exams", []))
                    writer.writerow([
                        state,
                        i.get("name", ""),
                        i.get("type", ""),
                        i.get("location", ""),
                        i.get("category", ""),
                        i.get("established", ""),
                        i.get("ranking", ""),
                        i.get("website", ""),
                        exams
                    ])
        print("✅ Exported Python INSTITUTES_DATA to institutes_data.csv")
    except Exception as e:
        print(f"❌ Error exporting Institutes data: {e}")

def export_exams_to_csv():
    try:
        with open("exams_data.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            # Headers
            writer.writerow(["Name", "Full Name", "Target", "Date", "Website", "Eligibility", "Syllabus", "Top Colleges"])
            
            for e in NATIONAL_ENTRANCE_EXAMS:
                colleges = ", ".join(e.get("top_colleges", []))
                writer.writerow([
                    e.get("name", ""),
                    e.get("full_name", ""),
                    e.get("for", ""),
                    e.get("date", ""),
                    e.get("link", ""),
                    e.get("eligibility", ""),
                    e.get("syllabus", ""),
                    colleges
                ])
        print("✅ Exported Python EXAMS_DATA to exams_data.csv")
    except Exception as e:
        print(f"❌ Error exporting Exams data: {e}")

if __name__ == "__main__":
    print("Starting data extraction to CSV (Excel compatible)...")
    export_sqlite_to_csv()
    export_institutes_to_csv()
    export_exams_to_csv()
    print("✨ All data extracted successfully!")
