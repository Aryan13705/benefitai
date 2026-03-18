import sqlite3
import os

def insert_extracted_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "schemes.db")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    extracted_schemes = [
      {
        "name": "PM Vishwakarma scheme",
        "description": "Provides information about PM Vishwakarma scheme to support traditional artisans and craftspeople of rural and urban India.",
        "apply_link": "https://en.vikaspedia.in/social-welfare/government-schemes/schemes-for-all-sections/pm-vishwakarma-scheme"
      },
      {
        "name": "Schemes for Anganwadi workers",
        "description": "Provides information about various welfare and support schemes dedicated to Anganwadi workers.",
        "apply_link": "https://en.vikaspedia.in/social-welfare/government-schemes/schemes-for-all-sections/schemes-for-anganwadi-workers"
      },
      {
        "name": "Mera Gaon Meri Dharohar",
        "description": "Provides information about the Mera Gaon Meri Dharohar scheme aimed at documenting and preserving village heritage.",
        "apply_link": "https://en.vikaspedia.in/social-welfare/government-schemes/schemes-for-all-sections/mera-gaon-meri-dharohar"
      },
      {
        "name": "ICMR Centenary Post Doctoral Fellowship",
        "description": "Provides details on the ICMR Centenary Post Doctoral Fellowship (ICMR-PDF) for medical and health researchers.",
        "apply_link": "https://en.vikaspedia.in/education/schemes-for-students/fellowships/icmr-centenary-post-doctoral-fellowship"
      },
      {
        "name": "PM-E-Drive Scheme",
        "description": "Promotion of Electric Mobility through Electric Vehicle (EV) subsidies.",
        "apply_link": "https://en.vikaspedia.in/social-welfare/government-schemes/schemes-for-all-sections/pm-e-drive-scheme"
      },
      {
        "name": "Schemes for Entrepreneurs",
        "description": "A comprehensive list of schemes and incentives provided by the government to support new and existing entrepreneurs.",
        "apply_link": "https://en.vikaspedia.in/social-welfare/government-schemes/schemes-for-all-sections/schemes-for-entrepreneurs"
      },
      {
        "name": "Schemes for senior citizens",
        "description": "Provides information related to welfare, health, and financial security schemes for senior citizens.",
        "apply_link": "https://en.vikaspedia.in/social-welfare/government-schemes/schemes-for-all-sections/schemes-for-senior-citizens"
      },
      {
        "name": "Aatma Nirbhar Bharat Abhiyaan",
        "description": "Information on the various pillars and schemes under the Aatma Nirbhar Bharat (Self-Reliant India) initiative.",
        "apply_link": "https://en.vikaspedia.in/social-welfare/government-schemes/schemes-for-all-sections/aatma-nirbhar-bharat-abhiyaan"
      },
      {
        "name": "PM SVANidhi",
        "description": "Micro-credit facility for street vendors to facilitate collateral-free working capital loans.",
        "apply_link": "https://en.vikaspedia.in/social-welfare/government-schemes/schemes-for-street-vendors/pm-svanidhi"
      },
      {
        "name": "Pradhan Mantri Jan Dhan Yojana",
        "description": "National Mission for Financial Inclusion to ensure access to financial services namely, banking/ savings & deposit accounts, remittance, credit, insurance, pension in an affordable manner.",
        "apply_link": "https://en.vikaspedia.in/social-welfare/government-schemes/financial-inclusion/pradhan-mantri-jan-dhan-yojana"
      }
    ]
    
    for s in extracted_schemes:
        # Check for existing
        cursor.execute("SELECT id FROM opportunities WHERE name = ?", (s["name"],))
        if cursor.fetchone():
            print(f"Skipping existing: {s['name']}")
            continue
            
        type_choice = "Social Welfare"
        if "Fellowship" in s["name"] or "Education" in s["description"]:
            type_choice = "Scholarship"
        elif "Enterpreneurs" in s["name"] or "Business" in s["description"]:
            type_choice = "MSME"
            
        cursor.execute("""
        INSERT INTO opportunities (name, type, ministry, state, min_age, max_age, max_income, category, gender, education_level, deadline, apply_link, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            s["name"], 
            type_choice, 
            "Central Government", 
            "Central", 
            18, 60, 9999999, 
            "All", "All", "All", 
            "Open", 
            s["apply_link"], 
            s["description"]
        ))
        
    conn.commit()
    conn.close()
    print("Data insertion complete.")

if __name__ == "__main__":
    insert_extracted_data()
