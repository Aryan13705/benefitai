import sqlite3
import os

def migrate_db():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "schemes.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create new table with expanded schema
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS opportunities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        type TEXT NOT NULL, -- Scholarship, Internship, MSME, Startup
        ministry TEXT,
        state TEXT DEFAULT 'Central',
        min_age INTEGER DEFAULT 0,
        max_age INTEGER DEFAULT 100,
        max_income INTEGER DEFAULT 9999999,
        category TEXT DEFAULT 'All',
        gender TEXT DEFAULT 'All',
        education_level TEXT DEFAULT 'All',
        deadline TEXT,
        apply_link TEXT,
        description TEXT
    )
    """)

    # Populate with sample data
    sample_data = [
        # Scholarships
        ("Post-Matric Scholarship for SC Students", "Scholarship", "Ministry of Social Justice", "Central", 15, 25, 250000, "SC", "All", "10th Pass", "2026-03-31", "https://scholarships.gov.in", "Financial assistance for SC students pursuing post-matric courses."),
        ("Pragati Scholarship for Girls", "Scholarship", "AICTE", "Central", 16, 22, 800000, "All", "Female", "Degree/Diploma", "2026-12-31", "https://www.aicte-india.org", "Scholarship for girls pursuing technical education."),
        
        # Internships
        ("Digital India Internship Scheme", "Internship", "MeitY", "Central", 18, 25, 1000000, "All", "All", "B.E/B.Tech", "2026-05-15", "https://meity.gov.in", "Stipend-based internship in digital government projects."),
        ("NITI Aayog Internship", "Internship", "NITI Aayog", "Central", 20, 30, 1000000, "All", "All", "Undergraduate/Postgraduate", "2026-06-30", "https://niti.gov.in", "Work on public policy and research."),

        # MSME Schemes
        ("PMEGP Loan Scheme", "MSME", "Ministry of MSME", "Central", 18, 60, 9999999, "All", "All", "8th Pass", "Open", "https://kviconline.gov.in", "Credit linked subsidy program for setting up new micro-enterprises."),
        ("ASPIRE Scheme", "MSME", "Ministry of MSME", "Central", 18, 50, 9999999, "All", "All", "All", "Open", "https://msme.gov.in", "Scheme for promotion of innovation, rural industry and entrepreneurship."),

        # Startup Benefits
        ("Startup India Seed Fund", "Startup", "DPIIT", "Central", 18, 45, 9999999, "All", "All", "Any", "Open", "https://www.startupindia.gov.in", "Financial assistance to early-stage startups."),
        ("Gujarat Startup Subsidy", "Startup", "Govt of Gujarat", "Gujarat", 18, 40, 9999999, "All", "All", "Graduate", "2026-12-31", "https://startup.gujarat.gov.in", "Support for startups based in Gujarat."),
        
        # Adding some state-specific scholarships
        ("MahaDBT Scholarship", "Scholarship", "Govt of Maharashtra", "Maharashtra", 18, 25, 800000, "OBC", "All", "Graduate", "2026-04-15", "https://mahadbt.maharashtra.gov.in", "Scholarship for OBC students in Maharashtra.")
    ]

    cursor.executemany("""
    INSERT INTO opportunities (name, type, ministry, state, min_age, max_age, max_income, category, gender, education_level, deadline, apply_link, description)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, sample_data)

    conn.commit()
    conn.close()
    print("Database migrated and sample data added.")

if __name__ == "__main__":
    migrate_db()
