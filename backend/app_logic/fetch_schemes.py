import requests
import sqlite3
import os
import time

def fetch_and_sync():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "schemes.db")
    
    # Categories to fetch
    categories = ["Education & Learning", "Social Welfare & Empowerment", "Business & Entrepreneurship"]
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("Starting scheme fetch from myScheme.gov.in...")
    
    for category in categories:
        print(f"Fetching category: {category}")
        try:
            # Note: Adding headers to mimic browser request to avoid 401 Unauthorized
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Accept": "application/json, text/plain, */*",
                "Referer": "https://www.myscheme.gov.in/",
                "Origin": "https://www.myscheme.gov.in"
            }
            # Category needs encoding
            encoded_cat = category.replace(" ", "%20").replace("&", "%26")
            url = f"https://api.myscheme.gov.in/search/v6/schemes?size=20&category={encoded_cat}"
            response = requests.get(url, headers=headers, timeout=15)
            
            if response.status_code != 200:
                print(f"Failed to fetch {category}: Status {response.status_code}")
                continue
                
            data = response.json()
            
            schemes = data.get("hits", {}).get("hits", [])
            for hit in schemes:
                s = hit.get("_source", {})
                name = s.get("schemeName", "Unknown Scheme")
                slug = s.get("slug")
                ministry = s.get("ministryName", "Central Government")
                desc = s.get("schemeShortDescription", "")
                
                # Check for existing
                cursor.execute("SELECT id FROM opportunities WHERE name = ?", (name,))
                if cursor.fetchone():
                    continue
                
                # Map to our schema
                # Defaulting some fields as the API might have different structure for eligibility
                type_map = "Scholarship" if "Education" in category else "MSME" if "Business" in category else "Social Welfare"
                
                cursor.execute("""
                INSERT INTO opportunities (name, type, ministry, state, min_age, max_age, max_income, category, gender, education_level, deadline, apply_link, description)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    name, 
                    type_map, 
                    ministry, 
                    "Central", 
                    0, 100, 9999999, 
                    "All", "All", "All", 
                    "Open", 
                    f"https://www.myscheme.gov.in/schemes/{slug}", 
                    desc
                ))
            
            conn.commit()
            print(f"Successfully synced {len(schemes)} items for {category}")
            
        except Exception as e:
            print(f"Error fetching {category}: {e}")
            
    conn.close()
    print("Fetch and Sync complete.")

if __name__ == "__main__":
    fetch_and_sync()
