from flask import Flask, request, session, jsonify
import datetime
import random
import string
# import pandas as pd # Moved to function scope to speed up Vercel startup
from functools import wraps
# from locations import INDIAN_STATES_UNIVERSITIES # Moved to local function scope
# from students_data import STATES_DATA, UNIVERSITY_DATA, CENTRAL_SCHEMES # Moved to local function scope
# from institutes_data import INSTITUTES_DATA, NATIONAL_ENTRANCE_EXAMS # Moved to local function scope
import time
import os

# Define base directory for backend resources
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# App Logic directory
APP_LOGIC_DIR = os.path.join(BASE_DIR, "app_logic")
import sys
sys.path.append(APP_LOGIC_DIR)

# -------------------------
# ADMIN DECORATOR
# -------------------------
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            return jsonify({"status": "error", "message": "Admin access required."}), 403
        return f(*args, **kwargs)
    return decorated_function

# --- NEWS CACHE ---
# Updated to use India Today English Feed as requested
INDIA_TODAY_RSS = "https://www.indiatoday.in/rss/home"
NEWS_CACHE = {
    "data": [],
    "last_update": 0
}
CACHE_DURATION = 3600  # 1 hour (More frequent updates)
import feedparser
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import firebase_admin
from firebase_admin import credentials, firestore, storage
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load local .env file for development (Vercel uses environment variables)
load_dotenv()

# -------------------------
# FIREBASE ADMIN SETUP (LAZY)
# -------------------------
firebase_db = None

def get_firebase_db():
    global firebase_db
    if firebase_db is not None:
        return firebase_db
        
    try:
        # 1. Try environment variable (JSON string) for production (Vercel)
        service_account_json = os.environ.get("FIREBASE_SERVICE_ACCOUNT")
        
        if service_account_json:
            # some users paste Base64 encoded JSON to avoid quoting issues
            try:
                if not service_account_json.strip().startswith("{"):
                    import base64
                    service_account_json = base64.b64decode(service_account_json).decode('utf-8')
                    print("[FIREBASE] Decoded service account from base64.")
            except Exception:
                # not base64 or decode failed; continue with original value
                pass

            import json
            try:
                service_account_info = json.loads(service_account_json)
            except Exception as e:
                print(f"[FIREBASE] Failed to parse JSON from env var: {e}")
                service_account_info = None

            if service_account_info:
                # Fix for escaped newlines in environment variables
                if "private_key" in service_account_info:
                    service_account_info["private_key"] = service_account_info["private_key"].replace("\\n", "\n")
                
                cred = credentials.Certificate(service_account_info)
                if not firebase_admin._apps:
                    firebase_admin.initialize_app(cred, {'storageBucket': 'benefitai.appspot.com'})
                firebase_db = firestore.client()
                print("[FIREBASE] Admin SDK initialized via env variable.")
            else:
                print("[FIREBASE] Environment variable provided but JSON parsing failed.")
        # 2. Fallback to local file for development
        elif os.path.exists(os.path.join(BASE_DIR, "firebase-adminsdk.json")):
            cred = credentials.Certificate(os.path.join(BASE_DIR, "firebase-adminsdk.json"))
            if not firebase_admin._apps:
                firebase_admin.initialize_app(cred, {'storageBucket': 'benefitai.appspot.com'})
            firebase_db = firestore.client()
            print("[FIREBASE] Admin SDK initialized with local service account file.")
        else:
            print(f"[FIREBASE] Service account missing at {os.path.join(BASE_DIR, 'firebase-adminsdk.json')}. Please set FIREBASE_SERVICE_ACCOUNT env var or place it in the backend folder.")
    except Exception as e:
        print(f"[FIREBASE ERROR] Lazy init failed: {e}")
    
    return firebase_db


app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev_secret_key_benefitai_2026")

# session cookies need to be cross-site because frontend and backend are separate
app.config.update({
    "SESSION_COOKIE_SAMESITE": "Lax",
    "SESSION_COOKIE_SECURE": False,
    "SESSION_COOKIE_HTTPONLY": True,
    "PERMANENT_SESSION_LIFETIME": datetime.timedelta(days=7),
    "REMEMBER_COOKIE_DURATION": datetime.timedelta(days=7),
    "REMEMBER_COOKIE_SAMESITE": "Lax",
    "REMEMBER_COOKIE_SECURE": False,
})

# Allow requests from the frontend — specify origins for credentials support
ALLOWED_ORIGINS = [
    # Local development
    "http://localhost:3000", 
    "http://127.0.0.1:3000", 
    "http://localhost:5000",
    "http://localhost:5002",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    # Netlify deployments
    "https://jazzy-shortbread-8b80b6.netlify.app",
    "https://benefitai.netlify.app",
    "https://benefitai.firebaseapp.com",
    "https://benefitai.web.app",
]

# Dynamic CORS configuration that allows Render/Vercel domains
def get_cors_origins():
    origins = []
    import re
    for origin in ALLOWED_ORIGINS:
        if "*" in origin:
            # Convert wildcard to regex pattern if needed, but for now just include them
            # flask-cors handles strings in the list.
            origins.append(origin)
        else:
            origins.append(origin)
    # Add dynamic origins from environment if set
    if os.environ.get("FRONTEND_URL"):
        origins.append(os.environ.get("FRONTEND_URL"))
    return origins if origins else ["*"]

CORS(app, 
     supports_credentials=True, 
     origins=get_cors_origins() or True,  # Allow all if no specific origins
     allow_headers=["Content-Type", "Authorization"],
     methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])

def _normalize_excel_scheme(row: dict) -> dict:
    """
    Convert a raw row from NSP_Scholarships_FINAL_STANDARDIZED.xlsx into the
    same shape used throughout the app (same keys as Firestore documents).
    """
    edu = str(row.get("Education_Level") or "All").strip()

    # Map Excel education strings → canonical app values
    EDU_MAP = {
        "Class 1-10":               "School",
        "Class 9-10":               "Class 9-10",
        "Class 9-12":               "Class 9-12",
        "Class 11-PG":              "Senior Secondary",
        "UG-PG":                    "Graduate",
        "Technical Diploma-Degree": "Diploma",
        "Professional UG-PG":       "Graduate",
    }
    edu_canonical = EDU_MAP.get(edu, edu)

    return {
        # Core identity
        "id":              f"excel_{row.get('Scheme_Name', '')}",
        "name":            str(row.get("Scheme_Name") or "").strip(),
        "ministry":        str(row.get("Ministry")    or "NSP").strip(),
        "type":            "Scholarship",
        "source":          "excel",  # provenance flag

        # Eligibility
        "state":           "Central",      # all NSP schemes are central
        "min_age":         int(row.get("Min_Age")    or 0),
        "max_age":         int(row.get("Max_Age")    or 99),
        "max_income":      int(row.get("Max_Income") or 9_999_999),
        "category":        str(row.get("Category")  or "All").strip(),
        "gender":          str(row.get("Gender")     or "All").strip(),
        "education_level": edu_canonical,
        "education_raw":   edu,           # keep original for UI display

        # Application info
        "deadline":        str(row.get("Deadline")   or "").strip(),
        "apply_link":      str(row.get("Apply_Link") or "").strip(),
        "description":     f"{row.get('Scheme_Name', '')} — National Scholarship Portal (NSP)",
        "documents":       [d.strip() for d in str(row.get("Documents") or "").split(",") if d.strip()],
    }


# ─── Excel cache (loaded once per process) ───────────────────────────────────
_EXCEL_SCHEMES: list = []
_EXCEL_LOADED:  bool = False

def _load_excel_schemes() -> list:
    """Load NSP scholarships from the bundled Excel file (cached after first call)."""
    global _EXCEL_SCHEMES, _EXCEL_LOADED
    if _EXCEL_LOADED:
        return _EXCEL_SCHEMES

    candidates = [
        os.path.join(BASE_DIR, "NSP_Scholarships_FINAL_STANDARDIZED.xlsx"),
        os.path.join(os.path.dirname(BASE_DIR), "NSP_Scholarships_FINAL_STANDARDIZED.xlsx"),
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                import pandas as pd
                df = pd.read_excel(path)
                df = df.where(pd.notnull(df), None)
                _EXCEL_SCHEMES = [_normalize_excel_scheme(r) for _, r in df.iterrows()]
                _EXCEL_LOADED = True
                print(f"[EXCEL] Loaded {len(_EXCEL_SCHEMES)} NSP schemes from {path}")
                return _EXCEL_SCHEMES
            except Exception as e:
                print(f"[EXCEL ERROR] Failed to load {path}: {e}")

    print("[EXCEL] NSP Excel file not found — skipping Excel source.")
    _EXCEL_LOADED = True   # don't retry every request
    return []


def get_all_schemes() -> list:
    """
    Return merged scheme list from THREE sources (priority order):
      1. Firestore  — admin-managed / custom schemes
      2. Excel file — NSP_Scholarships_FINAL_STANDARDIZED.xlsx (bundled)
    Duplicates (same name) from lower-priority sources are dropped.
    """
    seen_names: set = set()
    merged:     list = []

    # ── Source 1: Firestore ──────────────────────────────────────────────────
    db = get_firebase_db()
    if db:
        try:
            docs = db.collection("schemes").stream()
            for doc in docs:
                scheme = doc.to_dict()
                if "id" not in scheme:
                    scheme["id"] = doc.id
                scheme.setdefault("source", "firestore")
                name = str(scheme.get("name", "")).strip()
                if name and name not in seen_names:
                    seen_names.add(name)
                    merged.append(scheme)
        except Exception as e:
            print(f"[FIREBASE ERROR] Failed to fetch schemes: {e}")
    else:
        print("[SCHEMES] Firestore unavailable — using Excel only.")

    # ── Source 2: Excel file ─────────────────────────────────────────────────
    for scheme in _load_excel_schemes():
        name = scheme.get("name", "").strip()
        if name and name not in seen_names:
            seen_names.add(name)
            merged.append(scheme)

    print(f"[SCHEMES] Total merged: {len(merged)} "
          f"(firestore={sum(1 for s in merged if s.get('source')=='firestore')}, "
          f"excel={sum(1 for s in merged if s.get('source')=='excel')})")
    return merged


# -------------------------
# LOGIN MANAGER SETUP
# -------------------------
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.unauthorized_handler
def unauthorized():
    return jsonify({"status": "error", "message": "Unauthorized. Please log in.", "redirect": "/login.html"}), 401


# -------------------------
# USER CLASS
# -------------------------
class User(UserMixin):
    def __init__(self, id, name, email, password, role,
                 dob=None, gender=None, category=None, income=0,
                 education=None, employment_status=None, state_residence=None,
                 university=None, address=None, profile_complete=0, profile_pic=None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.dob = dob
        self.gender = gender
        self.category = category
        self.income = income
        self.education = education
        self.employment_status = employment_status
        self.state_residence = state_residence
        self.university = university
        self.address = address
        self.profile_complete = profile_complete
        self.profile_pic = profile_pic

    @property
    def is_admin(self):
        return self.email == "aryan13705@gmail.com"


@login_manager.user_loader
def load_user(user_id):
    db = get_firebase_db()
    if not db:
        return None
    try:
        user_doc = db.collection("users").document(str(user_id)).get()
        if user_doc.exists:
            user = user_doc.to_dict()
            # Ensure ID is present in the object
            user_id_val = int(user_id) if str(user_id).isdigit() else user_id
            return User(
                user_id_val, user.get("name"), user.get("email"), user.get("password"), user.get("role"),
                user.get("dob"), user.get("gender"), user.get("category"), user.get("income", 0),
                user.get("education"), user.get("employment_status"), user.get("state_residence"),
                user.get("university"), user.get("address"), user.get("profile_complete", 0),
                user.get("profile_pic")
            )
    except Exception as e:
        print(f"[FIREBASE ERROR] load_user failed: {e}")
    return None


# -------------------------
# HOME — status check
# -------------------------
@app.route("/")
def index():
    if current_user.is_authenticated:
        return jsonify({"authenticated": True, "redirect": "/dashboard"})
    return jsonify({"authenticated": False})


# -------------------------
# HEALTH CHECK — for debugging
# -------------------------
@app.route("/health")
def health():
    """Simple health check endpoint for debugging"""
    return jsonify({
        "status": "ok",
        "service": "BenefitAI Backend",
        "firebase": "connected" if get_firebase_db() else "error"
    })


# -------------------------
# REGISTER
# -------------------------
@app.route("/register", methods=["POST"])
def register():
    db = get_firebase_db()
    if not db:
        return jsonify({"status": "error", "message": "Firebase not connected"}), 500

    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    password = generate_password_hash(data.get("password"), method="pbkdf2:sha256", salt_length=16)

    if not name or not email or not password:
        return jsonify({"status": "error", "message": "Name, email, and password are required"}), 400

    try:
        # Check if user already exists
        users_ref = get_firebase_db().collection("users").where("email", "==", email).limit(1).get()
        if users_ref:
            return jsonify({"status": "error", "message": "Email already exists."}), 409
        
        # Create new user in Firestore
        user_data = {
            "name": name,
            "email": email,
            "password": password,
            "role": "user",
            "profile_complete": 0,
            "created_at": datetime.datetime.now(datetime.timezone.utc)
        }
        user_ref = get_firebase_db().collection("users").document()
        user_ref.set(user_data)
        
        # Log in the user
        user_obj = User(
            user_ref.id, name, email, password, "user",
            None, None, None, 0, None, None, None, None, None, 0
        )
        login_user(user_obj)
        return jsonify({"status": "success", "redirect": "/profile_setup.html"})
    except Exception as e:
        print(f"[FIREBASE REGISTER ERROR] {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


# -------------------------
# LOGIN
# -------------------------
@app.route("/login", methods=["POST"])
def login():
    db = get_firebase_db()
    if not db:
        return jsonify({"status": "error", "message": "Firebase not connected"}), 500

    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    try:
        users_ref = get_firebase_db().collection("users").where("email", "==", email).limit(1).get()
        if not users_ref:
            return jsonify({"status": "error", "message": "Invalid credentials."}), 401
            
        user_doc = users_ref[0]
        user = user_doc.to_dict()

        if user.get("password") == "firebase_auth_managed":
            return jsonify({
                "status": "error", 
                "message": "This account was created via Google. Please use 'Forgot Password' to set an email password."
            }), 401
            
        if check_password_hash(user["password"], password):
            user_obj = User(
                user_doc.id, user.get("name"), user.get("email"), user.get("password"), user.get("role"),
                user.get("dob"), user.get("gender"), user.get("category"), user.get("income", 0),
                user.get("education"), user.get("employment_status"), user.get("state_residence"),
                user.get("university"), user.get("address"), user.get("profile_complete", 0),
                user.get("profile_pic")
            )
            login_user(user_obj, remember=True)
            if user_obj.email == "aryan13705@gmail.com":
                return jsonify({"status": "success", "redirect": "/admin.html"})
            if not user_obj.profile_complete:
                return jsonify({"status": "success", "redirect": "/profile_setup.html"})
            return jsonify({"status": "success", "redirect": "/dashboard.html"})

    except Exception as e:
         return jsonify({"status": "error", "message": str(e)}), 500

    return jsonify({"status": "error", "message": "Invalid credentials."}), 401


# -------------------------
# FIREBASE LOGIN / REGISTER
# -------------------------
@app.route("/firebase-login", methods=["POST"])
def firebase_login():
    db = get_firebase_db()
    if not db:
        return jsonify({"status": "error", "message": "Firebase not connected"}), 500

    data = request.get_json()
    email = data.get("email")
    name = data.get("name", "Firebase User")
    uid = data.get("uid")

    if not email:
        return jsonify({"status": "error", "message": "Email is required"}), 400

    try:
        users_ref = get_firebase_db().collection("users").where("email", "==", email).limit(1).get()
        
        if not users_ref:
            # Create user in Firestore
            user_data = {
                "name": name,
                "email": email,
                "password": "firebase_auth_managed",
                "role": "user",
                "profile_complete": 0
            }
            user_ref = get_firebase_db().collection("users").document()
            user_ref.set(user_data)
            user_id = user_ref.id
            user_dict = user_data
        else:
            user_doc = users_ref[0]
            user_id = user_doc.id
            user_dict = user_doc.to_dict()

        user_obj = User(
            user_id, user_dict.get("name"), user_dict.get("email"), user_dict.get("password"), user_dict.get("role"),
            user_dict.get("dob"), user_dict.get("gender"), user_dict.get("category"), user_dict.get("income", 0),
            user_dict.get("education"), user_dict.get("employment_status"), user_dict.get("state_residence"),
            user_dict.get("university"), user_dict.get("address"), user_dict.get("profile_complete", 0),
            user_dict.get("profile_pic")
        )
        login_user(user_obj, remember=True)
        
        if user_obj.email == "aryan13705@gmail.com":
            return jsonify({"status": "success", "redirect": "/admin.html"})
        if not user_obj.profile_complete:
            return jsonify({"status": "success", "redirect": "/profile_setup.html"})
        return jsonify({"status": "success", "redirect": "/dashboard.html"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# -------------------------
# PROFILE COMPLETION
# -------------------------
@app.route("/complete-profile", methods=["POST"])
@login_required
def complete_profile():
    db = get_firebase_db()
    if not db:
        return jsonify({"status": "error", "message": "Firebase not connected"}), 500

    data = request.get_json()
    dob = data.get("dob")
    gender = data.get("gender")
    category = data.get("category")
    try:
        income = int(data.get("income", 0))
    except (ValueError, TypeError):
        income = 0
    education = data.get("education")
    employment_status = data.get("employment_status")
    state_residence = data.get("state_residence")
    university = data.get("university")
    address = data.get("address")

    try:
        user_data = {
            "name": current_user.name, 
            "email": current_user.email,
            "dob": dob, 
            "gender": gender, 
            "category": category, 
            "income": income,
            "education": education, 
            "employment_status": employment_status,
            "state_residence": state_residence, 
            "university": university,
            "address": address,
            "profile_complete": 1,
            "last_updated": datetime.datetime.now(datetime.timezone.utc)
        }
        get_firebase_db().collection("users").document(str(current_user.id)).set(user_data, merge=True)
        return jsonify({"status": "success", "redirect": "/dashboard.html"})
    except Exception as e:
        print(f"[FIREBASE] Update failed: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


# -------------------------
# UPLOAD PROFILE PICTURE
# -------------------------
@app.route("/upload-profile-pic", methods=["POST"])
@login_required
def upload_profile_pic():
    db = get_firebase_db()
    if not db:
        return jsonify({"status": "error", "message": "Firebase not connected"}), 500

    if 'file' not in request.files:
        return jsonify({"status": "error", "message": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"status": "error", "message": "No selected file"}), 400

    try:
        # Upload to Firebase Storage
        bucket = storage.bucket()
        blob = bucket.blob(f"profile_pics/{current_user.id}")
        
        # Determine content type
        content_type = file.content_type or "image/jpeg"
        blob.upload_from_file(file, content_type=content_type)
        
        # Make it public
        blob.make_public()
        image_url = blob.public_url

        # Update Firestore
        db.collection("users").document(str(current_user.id)).update({
            "profile_pic": image_url
        })
        
        # Update current user object in session
        current_user.profile_pic = image_url
        
        return jsonify({"status": "success", "url": image_url})
    except Exception as e:
        print(f"[UPLOAD ERROR] {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


# -------------------------
# GET CURRENT USER INFO
# -------------------------
@app.route("/me")
@login_required
def me():
    return jsonify({
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        "profile_complete": current_user.profile_complete,
        "gender": current_user.gender,
        "category": current_user.category,
        "income": current_user.income,
        "education": current_user.education,
        "state_residence": current_user.state_residence,
        "dob": current_user.dob,
        "address": current_user.address,
        "profile_pic": current_user.profile_pic
    })


# -------------------------
# EMAIL OTP SYSTEM (MOCK)
# -------------------------
@app.route("/send-otp", methods=["POST"])
def send_otp():
    data = request.get_json()
    email = data.get("email")
    if not email:
        return jsonify({"status": "error", "message": "Email is required"}), 400

    otp = "".join([str(random.randint(0, 9)) for _ in range(6)])
    session[f"otp_{email}"] = otp

    # SEND REAL EMAIL
    sender_email = os.environ.get("SMTP_EMAIL")
    sender_password = os.environ.get("SMTP_PASSWORD")

    if not sender_email or not sender_password or sender_email == "your_email@gmail.com":
        msg_log = f"⚠️ SMTP not configured! Showing OTP in terminal for {email}: {otp}"
        print(msg_log)
        with open(os.path.join(BASE_DIR, "otp.txt"), "w") as f: f.write(otp)
        # Store OTP in a local file or just terminal, but NOT in session if we want to be secure.
        # However, we NEED to verify it. So we store it in a global dict for now (since it's a dev server).
        if not hasattr(app, 'otp_store'): app.otp_store = {}
        app.otp_store[email] = otp
        return jsonify({"status": "success", "message": "Verification code sent! (Check backend logs for code)"})

    try:
        msg = MIMEMultipart()
        msg['From'] = f"BenefitAI <{sender_email}>"
        msg['To'] = email
        msg['Subject'] = "Your BenefitAI Verification Code"

        html_body = f"""
        <html>
          <body>
            <h2>Welcome to BenefitAI</h2>
            <p>Your one-time verification code is:</p>
            <h1 style="color: #4f46e5; letter-spacing: 5px;">{otp}</h1>
            <p>This code will expire in 10 minutes. If you did not request this, please ignore this email.</p>
          </body>
        </html>
        """
        msg.attach(MIMEText(html_body, 'html'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print(f"[EMAIL] Successfully sent OTP to {email}")
        return jsonify({"status": "success", "message": "OTP sent successfully"})
    except Exception as e:
        print(f"[EMAIL ERROR] Failed to send email to {email}: {e}")
        return jsonify({"status": "error", "message": f"Failed to send email: {str(e)}"}), 500


@app.route("/verify-otp", methods=["POST"])
def verify_otp():
    data = request.get_json()
    email = data.get("email")
    otp_input = data.get("otp")

    if not email or not otp_input:
        return jsonify({"status": "error", "message": "Email and OTP are required"}), 400

    stored_otp = session.get(f"otp_{email}")
    if not stored_otp and hasattr(app, 'otp_store'):
        stored_otp = app.otp_store.get(email)

    if stored_otp and stored_otp == otp_input:
        session.pop(f"otp_{email}", None)
        if hasattr(app, 'otp_store'): app.otp_store.pop(email, None)
        return jsonify({"status": "success", "message": "OTP verified"})
    return jsonify({"status": "error", "message": "Invalid or expired OTP"}), 400


@app.route("/forgot-password", methods=["POST"])
def forgot_password():
    db = get_firebase_db()
    if not db:
        return jsonify({"status": "error", "message": "Firebase not connected"}), 500

    data = request.get_json()
    email = data.get("email")
    if not email:
        return jsonify({"status": "error", "message": "Email is required"}), 400

    try:
        users_ref = get_firebase_db().collection("users").where("email", "==", email).limit(1).get()
        if not users_ref:
            return jsonify({"status": "error", "message": "User not found"}), 404
        user = users_ref[0].to_dict()
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

    otp = "".join([str(random.randint(0, 9)) for _ in range(6)])
    session[f"reset_otp_{email}"] = otp

    # Re-use the SMTP logic
    sender_email = os.environ.get("SMTP_EMAIL")
    sender_password = os.environ.get("SMTP_PASSWORD")

    if not sender_email or not sender_password or sender_email == "your_email@gmail.com":
        print(f"⚠️ SMTP not configured! Showing Reset OTP in terminal for {email}: {otp}")
        return jsonify({"status": "success", "message": "Reset OTP logic hit (check terminal)"})

    try:
        msg = MIMEMultipart()
        msg['From'] = f"BenefitAI Support <{sender_email}>"
        msg['To'] = email
        msg['Subject'] = "Reset Your BenefitAI Password"

        html_body = f"""
        <html>
          <body>
            <h2>Password Reset Request</h2>
            <p>Your one-time password reset code is:</p>
            <h1 style="color: #4f46e5; letter-spacing: 5px;">{otp}</h1>
            <p>Use this code to verify your identity. If you did not request this, please ignore this email.</p>
          </body>
        </html>
        """
        msg.attach(MIMEText(html_body, 'html'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        return jsonify({"status": "success", "message": "Reset OTP sent successfully"})
    except Exception as e:
        print(f"[EMAIL ERROR] Failed to send reset email to {email}: {e}")
        return jsonify({"status": "error", "message": "Failed to send reset email"}), 500


@app.route("/verify-reset-otp", methods=["POST"])
def verify_reset_otp():
    data = request.get_json()
    email = data.get("email")
    otp_input = data.get("otp")

    if not email or not otp_input:
        return jsonify({"status": "error", "message": "Email and OTP are required"}), 400

    stored_otp = session.get(f"reset_otp_{email}")
    if not stored_otp or stored_otp != otp_input:
        return jsonify({"status": "error", "message": "Invalid or expired OTP"}), 400

    # Set a flag in session that this email is verified for reset
    session[f"reset_verified_{email}"] = True
    session.pop(f"reset_otp_{email}", None)
    return jsonify({"status": "success", "message": "OTP verified"})


@app.route("/reset-password", methods=["POST"])
def reset_password():
    data = request.get_json()
    email = data.get("email")
    new_password = data.get("password")

    if not email or not new_password:
        return jsonify({"status": "error", "message": "Email and new password are required"}), 400

    if not session.get(f"reset_verified_{email}"):
        return jsonify({"status": "error", "message": "OTP verification required first"}), 403

    hashed_password = generate_password_hash(new_password, method="pbkdf2:sha256", salt_length=16)

    try:
        users_ref = get_firebase_db().collection("users").where("email", "==", email).limit(1).get()
        if not users_ref:
            return jsonify({"status": "error", "message": "User not found"}), 404
        
        user_doc = users_ref[0]
        user_doc.reference.update({"password": hashed_password})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

    session.pop(f"reset_verified_{email}", None)
    return jsonify({"status": "success", "message": "Password updated successfully"})


# -------------------------
# STATE & UNIVERSITY ROUTES
# -------------------------
@app.route("/get-universities", methods=["GET"])
def get_universities():
    from locations import INDIAN_STATES_UNIVERSITIES
    state = request.args.get("state")
    universities = INDIAN_STATES_UNIVERSITIES.get(state, [])
    return jsonify(universities)


@app.route("/set-location", methods=["POST"])
def set_location():
    data = request.get_json()
    state = data.get("state")
    university = data.get("university")
    if state:
        session["selected_state"] = state
    if university:
        session["selected_university"] = university
    return jsonify({"status": "success"})


# -------------------------
# LOGOUT
# -------------------------
@app.route("/logout", methods=["POST", "GET"])
@login_required
def logout():
    logout_user()
    return jsonify({"status": "success", "redirect": "/index.html"})


# ─────────────────────────────────────────────────────────────────────────────
# MATCHING ENGINE  (shared by /analyze, /dashboard, /recommendations)
# ─────────────────────────────────────────────────────────────────────────────

# Education hierarchy: higher index = higher level
# Uses EXACT token matching (not substring) to avoid 'class 1' ⊂ 'class 12' collisions
_EDU_LEVELS = [
    "class 1",   "class 9",  "class 10",  "class 9-10",
    "class 11",  "class 12", "class 9-12",
    "senior secondary", "diploma", "ug", "graduate",
    "pg", "postgraduate", "phd",
]

def _edu_rank(edu_str: str) -> int:
    """
    Return a numeric rank for an education string.
    Uses word-boundary matching so 'class 1' does NOT match 'class 12'.
    """
    import re
    s = edu_str.strip().lower()
    for i, token in enumerate(_EDU_LEVELS):
        # Build a regex that requires the token to match as a whole phrase
        pattern = r"(?<![0-9a-z])" + re.escape(token) + r"(?![0-9a-z])"
        if re.search(pattern, s):
            return i
    return -1   # unknown / "all"


def _edu_matches(user_edu: str, scheme_edu: str) -> bool:
    """
    True when the user's education level is eligible for the scheme's requirement.
    Handles exact tokens, 'All', and range strings like 'Class 9-12' / 'Class 11-PG'.
    """
    if not scheme_edu or scheme_edu.strip().lower() == "all":
        return True
    if not user_edu:
        return False

    s_low = scheme_edu.strip().lower()
    u_low = user_edu.strip().lower()

    # Direct substring match (e.g. "class 9-10" in "class 9-10")
    if u_low in s_low or s_low in u_low:
        return True

    # Range handling: "class 9-12", "class 11-pg", "ug-pg"
    if "-" in s_low:
        tokens = s_low.rsplit("-", 1)
        lo_str = tokens[0].strip()          # e.g. "class 9", "ug"
        hi_str = tokens[1].strip()          # e.g. "12", "pg", "degree"

        lo = _edu_rank(lo_str)

        # hi_str may be a bare number ("12") → reconstruct full class string
        if hi_str.isdigit():
            # Inherit the prefix from lo_str (e.g. "class" → "class 12")
            prefix = " ".join(lo_str.split()[:-1])   # "class 9" → "class"
            hi_full = f"{prefix} {hi_str}".strip() if prefix else hi_str
            hi = _edu_rank(hi_full)
        elif hi_str in ("pg", "postgraduate", "phd"):
            hi = 13
        else:
            hi = _edu_rank(hi_str)

        ur = _edu_rank(u_low)

        if lo != -1 and hi != -1 and ur != -1 and lo <= ur <= hi:
            return True

    return False


def score_scheme(scheme: dict, profile: dict) -> tuple[int, list[str]]:
    """
    Score a single scheme against a user profile.

    Parameters
    ----------
    scheme  : scheme dict (normalised)
    profile : dict with keys:
                age, income, category, gender, education, state,
                disability (bool), marks_10 (float), marks_12 (float)

    Returns
    -------
    (score: int, reasons: list[str])
      score  — 0-100; ≥ 60 is "eligible"
      reasons — human-readable strings explaining what matched
    """
    score   = 0
    reasons = []
    missing = []

    age       = int(profile.get("age")    or 0)
    income    = int(profile.get("income") or 0)
    category  = str(profile.get("category",  "General")).strip()
    gender    = str(profile.get("gender",    "Male")).strip()
    education = str(profile.get("education", "")).strip()
    state     = str(profile.get("state",     "Central")).strip()
    disability = bool(profile.get("disability", False))
    marks_10  = float(profile.get("marks_10") or 0)
    marks_12  = float(profile.get("marks_12") or 0)

    # ── 1. State / scope (hard filter) ──────────────────────────────── 20 pts
    scheme_state = str(scheme.get("state", "Central")).strip()
    if scheme_state == "Central" or scheme_state == state:
        score += 20
        if scheme_state == "Central":
            reasons.append("Central scheme — available in all states")
        else:
            reasons.append(f"State match ({state})")
    else:
        # Irrelevant state → immediately ineligible
        return 0, []

    # ── 2. Age ───────────────────────────────────────────────────────── 20 pts
    min_age = int(scheme.get("min_age") or 0)
    max_age = int(scheme.get("max_age") or 99)
    if age and min_age <= age <= max_age:
        score += 20
        reasons.append(f"Age eligible ({age} in {min_age}–{max_age})")
    elif age:
        missing.append(f"Age {age} outside {min_age}–{max_age}")

    # ── 3. Income ────────────────────────────────────────────────────── 20 pts
    max_income = int(scheme.get("max_income") or 9_999_999)
    if income and income <= max_income:
        score += 20
        reasons.append(f"Income eligible (₹{income:,} ≤ ₹{max_income:,})")
    elif income:
        missing.append(f"Income ₹{income:,} exceeds limit ₹{max_income:,}")

    # ── 4. Category ──────────────────────────────────────────────────── 15 pts
    scheme_cat = str(scheme.get("category", "All")).strip()
    if scheme_cat == "All" or scheme_cat.lower() == category.lower():
        score += 15
        reasons.append(f"Category match ({scheme_cat})")
    else:
        missing.append(f"Category mismatch (need {scheme_cat}, you are {category})")

    # ── 5. Gender ────────────────────────────────────────────────────── 10 pts
    scheme_gender = str(scheme.get("gender", "All")).strip()
    if scheme_gender == "All" or scheme_gender.lower() == gender.lower():
        score += 10
        if scheme_gender != "All":
            reasons.append(f"Gender-specific scholarship ({scheme_gender})")
    else:
        # Gender mismatch → hard disqualifier for gender-specific schemes
        return 0, []

    # ── 6. Education ─────────────────────────────────────────────────── 15 pts
    scheme_edu = str(scheme.get("education_level") or scheme.get("education_raw") or "All").strip()
    if _edu_matches(education, scheme_edu):
        score += 15
        reasons.append(f"Education eligible ({scheme_edu})")
    elif education:
        missing.append(f"Education mismatch (need {scheme_edu}, you have {education})")

    # ── 7. Disability bonus ──────────────────────────────────────────────── 5 pts
    scheme_name_lower = str(scheme.get("name", "")).lower()
    if disability and ("disabilit" in scheme_name_lower or "divyang" in scheme_name_lower
                       or "saksham" in scheme_name_lower):
        score += 5
        reasons.append("Disability-specific scheme — bonus match")

    # ── 8. Academic merit bonus ─────────────────────────────────────────── 5 pts
    avg_marks = (marks_10 + marks_12) / 2 if marks_10 and marks_12 else (marks_12 or marks_10)
    if avg_marks >= 85:
        score += 5
        reasons.append(f"High academic merit (avg {avg_marks:.1f}%)")
    elif avg_marks >= 70:
        score += 2
        reasons.append(f"Good academic marks (avg {avg_marks:.1f}%)")

    # Attach missing reasons for transparency
    if missing:
        reasons.append("⚠ Not matched: " + "; ".join(missing))

    return min(score, 100), reasons


# ─────────────────────────────────────────────────────────────────────────────
# ANALYZE — returns JSON scheme list
# ─────────────────────────────────────────────────────────────────────────────
@app.route("/analyze", methods=["POST"])
def analyze():
    """
    Accepts a profile payload and returns matched + ranked scholarships.

    Request body (all optional — sensible defaults applied):
    {
      "age":        18,
      "income":     200000,
      "category":   "SC",        // SC | ST | OBC | General | Minority | All
      "gender":     "Female",
      "education":  "Graduate",
      "state":      "Maharashtra",
      "disability": false,
      "marks_10":   85.5,
      "marks_12":   78.0,
      "min_score":  60           // override eligibility threshold (default 60)
    }
    """
    data = request.get_json() or {}

    # Build profile dict
    try:
        age    = int(data.get("age")    or 0)
        income = int(data.get("income") or 0)
    except (ValueError, TypeError):
        age = income = 0

    try:
        marks_10 = float(data.get("marks_10") or 0)
        marks_12 = float(data.get("marks_12") or 0)
    except (ValueError, TypeError):
        marks_10 = marks_12 = 0.0

    profile = {
        "age":        age,
        "income":     income,
        "category":   str(data.get("category",  "General")).strip(),
        "gender":     str(data.get("gender",     "Male")).strip(),
        "education":  str(data.get("education")  or data.get("education_level") or "").strip(),
        "state":      str(data.get("state",      "Central")).strip(),
        "disability": bool(data.get("disability", False)),
        "marks_10":   marks_10,
        "marks_12":   marks_12,
    }

    min_score = int(data.get("min_score") or 60)

    all_schemes = get_all_schemes()
    matched = []

    for scheme in all_schemes:
        sc, reasons = score_scheme(scheme, profile)
        if sc >= min_score:
            # Derive a deadline urgency flag
            deadline_str  = str(scheme.get("deadline") or "").strip()
            days_left     = None
            deadline_urgent = False
            if deadline_str:
                try:
                    d_date    = datetime.datetime.strptime(deadline_str, "%Y-%m-%d")
                    days_left = (d_date - datetime.datetime.now()).days
                    deadline_urgent = 0 <= days_left <= 30
                except ValueError:
                    pass

            matched.append({
                "scheme_name":      scheme.get("name", ""),
                "ministry":         scheme.get("ministry", ""),
                "type":             scheme.get("type", "Scholarship"),
                "state":            scheme.get("state", "Central"),
                "deadline":         deadline_str,
                "days_left":        days_left,
                "deadline_urgent":  deadline_urgent,
                "apply_link":       scheme.get("apply_link", ""),
                "description":      scheme.get("description", ""),
                "documents":        scheme.get("documents", []),
                "education_level":  scheme.get("education_raw") or scheme.get("education_level", ""),
                "match_score":      sc,
                "match_reasons":    reasons,
                "source":           scheme.get("source", "firestore"),
            })

    # Sort: highest score first, then most urgent deadline
    matched.sort(key=lambda x: (-x["match_score"], x["days_left"] if x["days_left"] is not None else 9999))

    return jsonify({
        "schemes": matched,
        "count":   len(matched),
        "profile": profile,   # echo back so frontend can confirm what was used
    })


# -------------------------
# DASHBOARD — returns JSON data
# -------------------------
@app.route("/dashboard")
@login_required
def dashboard():
    db = get_firebase_db()
    saved = []
    if db:
        try:
            saved_ref = db.collection("users").document(str(current_user.id)).collection("saved_schemes").get()
            saved = [doc.to_dict()["scheme_name"] for doc in saved_ref]
        except Exception as e:
            print(f"[FIREBASE DASHBOARD ERROR] {e}")
    
    # 1. Calculate Eligible Schemes (Score >= 60)
    all_schemes = get_all_schemes()
    
    eligible_count = 0
    deadlines_this_month = 0
    now = datetime.datetime.now(datetime.timezone.utc)
    
    if db and current_user.profile_complete:
        try:
            user_doc = db.collection("users").document(str(current_user.id)).get()
            raw_profile = user_doc.to_dict() if user_doc.exists else {}
            try:
                income = int(raw_profile.get("income", 0))
            except (ValueError, TypeError):
                income = 0

            dash_profile = {
                "age":       0,   # not stored at top level; skip age filter
                "income":    income,
                "category":  raw_profile.get("category",        "General"),
                "gender":    raw_profile.get("gender",           "Male"),
                "education": raw_profile.get("education",        ""),
                "state":     raw_profile.get("state_residence",  "Central"),
                "disability": False,
                "marks_10":  0,
                "marks_12":  0,
            }

            for scheme in all_schemes:
                sc, _ = score_scheme(scheme, dash_profile)
                if sc >= 60:
                    eligible_count += 1

                # Check deadlines this month
                dl = str(scheme.get("deadline") or "")
                if dl:
                    try:
                        d_date = datetime.datetime.strptime(dl, "%Y-%m-%d")
                        if d_date.month == now.month and d_date.year == now.year:
                            deadlines_this_month += 1
                    except ValueError:
                        pass

        except Exception as e:
            print(f"[DASHBOARD EVAL ERROR] {e}")

    # 3. Calculate Submitted Applications
    applications_submitted = 0
    if db:
        try:
            apps_ref = db.collection("applications").where("user_id", "==", current_user.id).get()
            applications_submitted = len(apps_ref)
        except Exception as e:
            pass

    # 3. Calculate Upcoming Exams
    upcoming_exams = 0
    from institutes_data import NATIONAL_ENTRANCE_EXAMS
    # Very crude text match for current month / next month strings
    current_month_str = now.strftime("%b")
    next_month_str = (now.replace(day=28) + datetime.timedelta(days=4)).strftime("%b")
    for exam in NATIONAL_ENTRANCE_EXAMS:
        if current_month_str in exam["date"] or next_month_str in exam["date"]:
            upcoming_exams += 1

    return jsonify({
        "name": current_user.name,
        "saved_schemes": saved,
        "profile_complete": current_user.profile_complete,
        "eligible_schemes": eligible_count,
        "applications_submitted": applications_submitted,
        "upcoming_exams": upcoming_exams,
        "deadlines_this_month": deadlines_this_month
    })


@app.route("/save_scheme", methods=["POST"])
@login_required
def save_scheme():
    db = get_firebase_db()
    if not db:
        return jsonify({"status": "error", "message": "Firebase not connected"}), 500
        
    data = request.get_json()
    scheme_name = data.get("scheme_name")

    try:
        get_firebase_db().collection("users").document(str(current_user.id)).collection("saved_schemes").document(scheme_name).set({
            "scheme_name": scheme_name,
            "saved_at": datetime.datetime.now(datetime.timezone.utc)
        })
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/delete_scheme", methods=["POST"])
@login_required
def delete_scheme():
    db = get_firebase_db()
    if not db:
        return jsonify({"status": "error", "message": "Firebase not connected"}), 500
        
    data = request.get_json()
    scheme_name = data.get("scheme_name")

    try:
        get_firebase_db().collection("users").document(str(current_user.id)).collection("saved_schemes").document(scheme_name).delete()
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# -------------------------
# ACTIVITY LOGGING
# -------------------------
@app.route("/log-activity", methods=["POST"])
def log_activity():
    data = request.get_json()
    action = data.get("action")
    details = data.get("details", {})
    page = data.get("page")

    event_data = {
        "user_id": current_user.id if current_user.is_authenticated else "anonymous",
        "user_email": current_user.email if current_user.is_authenticated else "anonymous",
        "action": action,
        "details": details,
        "page": page,
        "timestamp": datetime.datetime.now(datetime.timezone.utc),
        "platform": "web"
    }

    if firebase_db:
        try:
            firebase_db.collection("activities").add(event_data)
        except Exception as e:
            print(f"[FIREBASE] Error logging activity: {e}")

    print(f"[ACTIVITY LOG] {event_data['user_email']} | {action} on {page} | {details}")
    return jsonify({"status": "success"})


# -------------------------
# STUDENTS — schemes by state
# -------------------------
@app.route("/students")
def students():
    from students_data import STATES_DATA, CENTRAL_SCHEMES
    state = request.args.get("state", "")
    include_central = request.args.get("central", "true").lower() == "true"
    state_info = STATES_DATA.get(state, {})
    state_schemes = state_info.get("schemes", [])
    universities = state_info.get("universities", [])
    central = CENTRAL_SCHEMES if include_central else []

    return jsonify({
        "state": state,
        "emoji": state_info.get("emoji", "🏛️"),
        "color": state_info.get("color", "#2563eb"),
        "schemes": state_schemes,
        "central_schemes": central,
        "universities": universities,
        "all_states": [
            {"name": k, "emoji": v["emoji"], "color": v["color"]}
            for k, v in STATES_DATA.items()
        ]
    })


# -------------------------
# STATES LIST — for selector
# -------------------------
@app.route("/states-list")
def states_list():
    from students_data import STATES_DATA
    return jsonify([
        {"name": k, "emoji": v["emoji"], "color": v["color"]}
        for k, v in STATES_DATA.items()
    ])


# -------------------------
# UNIVERSITY INFO — exams + scholarships
# -------------------------
@app.route("/university-info")
def university_info():
    from students_data import UNIVERSITY_DATA
    uni = request.args.get("name", "")
    data = UNIVERSITY_DATA.get(uni)
    if not data:
        return jsonify({"error": "University not found", "entrance_exams": [], "scholarships": []}), 404
    return jsonify({
        "name": uni,
        "state": data.get("state", ""),
        "entrance_exams": data.get("entrance_exams", []),
        "scholarships": data.get("scholarships", []),
    })


# -------------------------
# INSTITUTES — by state, with filters
# -------------------------
@app.route("/institutes")
def institutes():
    from institutes_data import INSTITUTES_DATA
    state = request.args.get("state", "")
    category = request.args.get("category", "")      # e.g. Engineering, Medical, Management
    inst_type = request.args.get("type", "")          # Government / Private / Central

    state_info = INSTITUTES_DATA.get(state, {})
    institutes_list = state_info.get("institutes", [])

    # Apply filters
    if category:
        institutes_list = [i for i in institutes_list if category.lower() in i["category"].lower()]
    if inst_type:
        institutes_list = [i for i in institutes_list if inst_type.lower() in i["type"].lower()]

    return jsonify({
        "state": state,
        "emoji": state_info.get("emoji", "🏛️"),
        "color": state_info.get("color", "#2563eb"),
        "institutes": institutes_list,
        "total": len(institutes_list),
        "all_states": [
            {"name": k, "emoji": v["emoji"], "color": v["color"]}
            for k, v in INSTITUTES_DATA.items()
        ]
    })


# -------------------------
# NATIONAL ENTRANCE EXAMS
# -------------------------
@app.route("/national-exams")
def national_exams():
    from institutes_data import NATIONAL_ENTRANCE_EXAMS
    return jsonify(NATIONAL_ENTRANCE_EXAMS)


# -------------------------
# DEADLINE ALERT SYSTEM (SMTP)
# -------------------------
@app.route("/admin/send-alerts", methods=["POST"])
@admin_required
def send_alerts():
    # In a real app, this would run as a daily cron job.
    # Exposing as an endpoint for manual invocation / testing.
    db = get_firebase_db()
    if not db:
        return jsonify({"status": "error", "message": "Firebase not connected"}), 500

    all_schemes = get_all_schemes()

    now = datetime.datetime.now()
    target_date = now + datetime.timedelta(days=3)
    
    # 1. Find schemes exactly 3 days away
    closing_schemes = []
    for scheme in all_schemes:
        if scheme["deadline"]:
            try:
                d_date = datetime.datetime.strptime(scheme["deadline"], "%Y-%m-%d")
                if d_date.date() == target_date.date():
                    closing_schemes.append(scheme)
            except ValueError:
                pass
                
    if not closing_schemes:
        return jsonify({"status": "success", "message": "No schemes closing in exactly 3 days."}), 200

    # 2. Setup SMTP
    sender_email = os.environ.get("SMTP_EMAIL")
    sender_password = os.environ.get("SMTP_PASSWORD")
    if not sender_email or not sender_password or sender_email == "your_email@gmail.com":
        return jsonify({"status": "error", "message": "SMTP credentials not configured in backend/.env"}), 500

    # 3. Process Users
    emails_sent = 0
    try:
        users = get_firebase_db().collection("users").stream()
        
        # Connect to SMTP server once
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        for user_doc in users:
            user_data = user_doc.to_dict()
            profile = user_data.get("profile", {})
            if not profile: continue
            
            user_email = user_data.get("email")
            if not user_email: continue

            income = int(profile.get("income", 0))
            category = profile.get("category", "General")
            state = profile.get("state_residence", "Central")
            education = profile.get("education_level", "")

            # Check eligibility for closing schemes
            for scheme in closing_schemes:
                score = 0
                if income <= scheme["max_income"]: score += 30
                if category == scheme["category"] or scheme["category"] == "All": score += 25
                if state == scheme["state"] or scheme["state"] == "Central": score += 20
                if education and education.lower() in scheme["education_level"].lower() or scheme["education_level"] == "All": score += 25
                
                # Penalize irrelevant states
                if scheme["state"] != state and scheme["state"] != "Central":
                    continue

                if score >= 80:  # Highly eligible!
                    try:
                        msg = MIMEMultipart()
                        msg['From'] = f"BenefitAI Alerts <{sender_email}>"
                        msg['To'] = user_email
                        msg['Subject'] = f"Urgent: {scheme['name']} Deadline Approaching!"
                        
                        body = f"""
                        <html>
                          <body style="font-family: Arial, sans-serif; color: #333;">
                            <h2 style="color: #dc2626;">Deadline Alert</h2>
                            <p>Hi,</p>
                            <p>Our AI engines show you are highly eligible for the <strong>{scheme['name']}</strong>, but the application window closes in exactly 3 days on {scheme['deadline']}.</p>
                            <p>Log in to <a href="http://localhost:3000/dashboard.html">BenefitAI</a> to apply instantly.</p>
                            <br>
                            <p>Best regards,<br>The BenefitAI Team</p>
                          </body>
                        </html>
                        """
                        msg.attach(MIMEText(body, 'html'))
                        server.send_message(msg)
                        emails_sent += 1
                    except Exception as email_err:
                        print(f"[SMTP ERROR] Failed to send to {user_email}: {email_err}")

        server.quit()
        return jsonify({
            "status": "success", 
            "message": f"Dispatched {emails_sent} alert emails for {len(closing_schemes)} schemes."
        }), 200

    except Exception as e:
        print(f"[ALERTS ERROR] {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


# -------------------------
# AI SCHEME RECOMMENDATION ENGINE
# -------------------------
@app.route("/recommendations", methods=["GET"])
@login_required
def recommendations():
    if not firebase_db:
        return jsonify([])

    try:
        user_doc = get_firebase_db().collection("users").document(str(current_user.id)).get()
        if not user_doc.exists:
            return jsonify([])
        
        profile = user_doc.to_dict()
        if not profile:
             return jsonify([])

        try:
            income = int(profile.get("income", 0))
        except (ValueError, TypeError):
            income = 0
        
        rec_profile = {
            "age":        0,
            "income":     income,
            "category":   profile.get("category",       "General"),
            "gender":     profile.get("gender",          "Male"),
            "education":  profile.get("education",       ""),
            "state":      profile.get("state_residence", "Central"),
            "disability": False,
            "marks_10":   0,
            "marks_12":   0,
        }

        all_schemes = get_all_schemes()

        scored_schemes = []
        for scheme in all_schemes:
            sc, reasons = score_scheme(scheme, rec_profile)
            if sc > 0:
                scored_schemes.append({
                    "scheme_name":     scheme.get("name", ""),
                    "ministry":        scheme.get("ministry", ""),
                    "type":            scheme.get("type", "Scholarship"),
                    "match_percentage": sc,
                    "match_reasons":   reasons,
                    "state":           scheme.get("state", "Central"),
                    "deadline":        str(scheme.get("deadline") or ""),
                    "apply_link":      scheme.get("apply_link", ""),
                    "documents":       scheme.get("documents", []),
                    "source":          scheme.get("source", "firestore"),
                })

        # Sort by highest score first
        scored_schemes.sort(key=lambda x: x["match_percentage"], reverse=True)
        top_5 = scored_schemes[:5]

        return jsonify(top_5), 200

    except Exception as e:
        print(f"[RECOMMENDATIONS ERROR] {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


# -------------------------
# DIRECT APPLICATION SYSTEM
# -------------------------
@app.route("/apply", methods=["POST"])
@login_required
def apply_scheme():
    try:
        scheme_name = request.form.get("scheme_name")
        if not scheme_name:
            return jsonify({"status": "error", "message": "Scheme name is required"}), 400

        user_id = current_user.id  # Email
        
        # Files validation
        required_files = ["income_cert", "caste_cert", "mark_sheet", "aadhaar"]
        uploaded_urls = {}
        
        if not firebase_db:
             return jsonify({"status": "error", "message": "Firebase not connected"}), 500

        bucket = storage.bucket()

        for file_key in required_files:
            file = request.files.get(file_key)
            if not file or file.filename == "":
                return jsonify({"status": "error", "message": f"Missing file: {file_key}"}), 400

            # Upload to Firebase Storage
            blob_path = f"applications/{user_id}/{scheme_name}/{file_key}_{file.filename}"
            blob = bucket.blob(blob_path)
            blob.upload_from_file(file, content_type=file.content_type)
            # blob.make_public()  # CRITICAL SECURITY FIX: Removed public access to sensitive documents
            # In production, use signed URLs or Firebase Security Rules for access.
            uploaded_urls[file_key] = blob_path # Store path instead of public URL for security

        # Save to Firestore
        app_ref = firebase_db.collection("applications").document()
        app_ref.set({
            "user_id": user_id,
            "scheme_name": scheme_name,
            "status": "Under Review",
            "submitted_date": datetime.datetime.utcnow().isoformat(),
            "documents": uploaded_urls
        })

        return jsonify({"status": "success", "message": "Application submitted successfully"}), 200

    except Exception as e:
        print(f"[APPLY ERROR] {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/my-applications", methods=["GET"])
@login_required
def my_applications():
    if not firebase_db:
        return jsonify([])
    
    try:
        apps_ref = firebase_db.collection("applications").where("user_id", "==", current_user.id).get()
        applications = []
        for doc in apps_ref:
            data = doc.to_dict()
            applications.append({
                "id": doc.id,
                "scheme_name": data.get("scheme_name"),
                "status": data.get("status"),
                "submitted_date": data.get("submitted_date"),
                "documents": data.get("documents", {})
            })
            
        # Sort by submitted_date descending
        applications.sort(key=lambda x: x["submitted_date"], reverse=True)
        return jsonify(applications), 200
    except Exception as e:
        print(f"[FETCH APPS ERROR] {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


# -------------------------
# FORUM ENDPOINTS
# -------------------------
@app.route("/api/forum", methods=["GET"])
@login_required
def get_forum_posts():
    if not firebase_db:
        return jsonify([])
    try:
        posts_ref = firebase_db.collection("forum_posts").get()
        posts = []
        for doc in posts_ref:
            p = doc.to_dict()
            p["id"] = doc.id
            posts.append(p)
        posts.sort(key=lambda x: x.get("created_at", ""), reverse=True)
        return jsonify(posts), 200
    except Exception as e:
        print(f"[FORUM GET ERROR] {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/api/forum", methods=["POST"])
@login_required
def create_forum_post():
    db = get_firebase_db()
    if not db:
        return jsonify({"status": "error", "message": "Firebase not connected"}), 500
    try:
        data = request.get_json()
        title = data.get("title")
        category = data.get("category")
        content = data.get("content")
        
        if not title or not category or not content:
            return jsonify({"status": "error", "message": "Missing required fields"}), 400
            
        new_post = {
            "title": title,
            "category": category,
            "content": content,
            "author_name": current_user.name,
            "author_id": current_user.id,
            "created_at": datetime.datetime.utcnow().isoformat(),
            "replies": []
        }
        
        firebase_db.collection("forum_posts").add(new_post)
        return jsonify({"status": "success", "message": "Post created"}), 201
    except Exception as e:
        print(f"[FORUM POST ERROR] {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


# Admin decorator moved to top

# -------------------------
# ADMIN ENDPOINTS
# -------------------------

@app.route("/admin/activities")
@admin_required
def get_admin_activities():
    db = get_firebase_db()
    if not db:
        return jsonify({"status": "error", "message": "Firebase not connected"}), 500
    try:
        # Fetch last 100 activities
        acts = firebase_db.collection("activities").order_by("timestamp", direction=firestore.Query.DESCENDING).limit(100).get()
        results = []
        for doc in acts:
            d = doc.to_dict()
            d["id"] = doc.id
            results.append(d)
        return jsonify(results)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/admin/schemes", methods=["GET", "POST"])
@admin_required
def admin_schemes():
    db = get_firebase_db()
    if not db:
        return jsonify({"status": "error", "message": "Firebase not connected"}), 500

    if request.method == "GET":
        return jsonify(get_all_schemes())
    
    if request.method == "POST":
        data = request.get_json()
        try:
            # Firestore will generate a document ID
            doc_ref = get_firebase_db().collection("schemes").document()
            data["id"] = doc_ref.id
            doc_ref.set(data)
            return jsonify({"status": "success", "id": doc_ref.id}), 201
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/admin/schemes/<scheme_id>", methods=["PUT", "DELETE"])
@admin_required
def admin_scheme_detail(scheme_id):
    db = get_firebase_db()
    if not db:
        return jsonify({"status": "error", "message": "Firebase not connected"}), 500

    if request.method == "DELETE":
        try:
            get_firebase_db().collection("schemes").document(str(scheme_id)).delete()
            return jsonify({"status": "success"})
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500
    
    if request.method == "PUT":
        data = request.get_json()
        try:
            data["id"] = scheme_id
            get_firebase_db().collection("schemes").document(str(scheme_id)).set(data, merge=True)
            return jsonify({"status": "success"})
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/admin/upload-schemes", methods=["POST"])
@admin_required
def upload_schemes():
    if 'file' not in request.files:
        return jsonify({"status": "error", "message": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"status": "error", "message": "No selected file"}), 400
        
    try:
        import pandas as pd
        import io
        filename = file.filename.lower()
        if filename.endswith('.csv'):
            df = pd.read_csv(io.StringIO(file.read().decode('utf-8')))
        elif filename.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(io.BytesIO(file.read()))
        else:
            return jsonify({"status": "error", "message": "Unsupported file format"}), 400
        
        # Mapping expected columns
        # name, type, ministry, state, min_age, max_age, max_income, category, gender, education_level, deadline, apply_link, description
        df = df.where(pd.notnull(df), None) # Convert NaN to None
        
        if not firebase_db:
            return jsonify({"status": "error", "message": "Firebase not connected"}), 500

        count = 0
        batch = get_firebase_db().batch()
        for _, row in df.iterrows():
            d = row.to_dict()
            doc_ref = firebase_db.collection("schemes").document()
            d["id"] = doc_ref.id
            batch.set(doc_ref, d)
            count += 1
            if count % 400 == 0: # Firestore batch limit is 500
                batch.commit()
                batch = firebase_db.batch()
        
        batch.commit()
        return jsonify({"status": "success", "count": count}), 201
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/suggest-universities", methods=["POST"])
def suggest_universities():
    from institutes_data import INSTITUTES_DATA
    data = request.json
    marks_10 = data.get("marks_10", 0)
    marks_12 = data.get("marks_12", 0)
    income = data.get("income", 9999999)
    
    suggestions = []
    
    # Flatten all institutes for easier filtering
    all_institutes = []
    for state, info in INSTITUTES_DATA.items():
        for inst in info["institutes"]:
            inst_copy = inst.copy()
            inst_copy["state_name"] = state
            all_institutes.append(inst_copy)

    avg_marks = (marks_10 + marks_12) / 2

    for inst in all_institutes:
        match_type = None
        ranking = inst.get("ranking", "").lower()
        inst_type = inst.get("type", "").lower()
        
        # Matching logic
        if avg_marks >= 90:
            if "iit" in ranking or "iisc" in ranking or "nirf #1" in ranking:
                match_type = "Elite"
            elif "nit" in ranking or "nirf #25" in ranking:
                match_type = "Competitive"
            else:
                match_type = "Match"
        elif avg_marks >= 75:
            if "iit" in ranking or "iisc" in ranking:
                continue
            elif "nit" in ranking or "nirf #50" in ranking:
                match_type = "Competitive"
            else:
                match_type = "Match"
        else:
            if "iit" in ranking or "nit" in ranking:
                continue
            match_type = "Match"

        # Financial filter
        if income < 250000:
            if "private" in inst_type:
                continue
        
        if match_type:
            inst["match_type"] = match_type
            suggestions.append(inst)

    priority_map = {"Elite": 1, "Competitive": 2, "Match": 3}
    suggestions.sort(key=lambda x: (priority_map.get(x["match_type"], 4), -x.get("established", 0)))
    
    return jsonify({
        "suggestions": suggestions[:12],
        "status": "success",
        "avg_marks": avg_marks
    })

@app.route("/suggest-institutes", methods=["POST"])
def suggest_institutes():
    from institutes_data import INSTITUTES_DATA
    data = request.json
    income = data.get("income", 9999999)
    preferred_states = data.get("states", [])
    category = data.get("category", "")
    marks_10 = data.get("marks_10", 0)
    marks_12 = data.get("marks_12", 0)
    jee_score = data.get("jee_score", 0)
    
    suggestions = []
    
    for state, info in INSTITUTES_DATA.items():
        if preferred_states and state not in preferred_states:
            continue
            
        for inst in info["institutes"]:
            if category and category != "All" and inst.get("category") != category:
                continue
                
            inst_copy = inst.copy()
            inst_copy["state_name"] = state
            
            inst_type = inst.get("type", "").lower()
            ranking = inst.get("ranking", "").lower()
            match_score = 0
            match_reason = ""
            
            # Base financial matching
            if income < 400000:
                if "government" in inst_type or "central" in inst_type or "nit" in inst_type or "iit" in inst_type:
                    match_score += 60
                    match_reason = "Affordable Gov/Central Institute (Low Fee)"
                else:
                    match_score += 30
                    match_reason = "Private - Check if scholarships are available"
            else:
                match_score += 40
                match_reason = "Reputed Regional Institute"

            # Academic Enhancements
            if "iit" in ranking or "nirf #1" in inst_type or "iisc" in ranking:
                if jee_score > 90 and marks_12 > 75:
                    match_score += 40
                    match_reason = "Elite Match! Your JEE score & academics fit IIT profiles."
            elif "nit" in ranking or "nirf #25" in ranking:
                if jee_score > 70 or marks_12 > 85:
                    match_score += 30
                    match_reason = "Great Match! Your academics fit NIT/Top Government profiles."
            elif "government" in inst_type:
                if marks_12 > 60:
                    match_score += 20
                    if not match_reason: match_reason = "Good academic fit for Government College."
            
            # Final scoring adjust
            inst_copy["match_score"] = min(100, match_score)
            inst_copy["match_reason"] = match_reason or "Balanced Match"
            suggestions.append(inst_copy)

    suggestions.sort(key=lambda x: x["match_score"], reverse=True)
    
    return jsonify({
        "suggestions": suggestions[:15],
        "status": "success"
    })

# -------------------------
# EXTERNAL NEWS API helpers
# -------------------------
import threading

def format_rss_date(entry):
    """
    Parses RSS entry date into human friendly format.
    Strictly uses 'Today, DD MMM' only for the current calendar day.
    """
    try:
        if not hasattr(entry, 'published_parsed') or not entry.published_parsed:
            return f"Today, {datetime.datetime.now().strftime('%d %b')}"
            
        published_dt = datetime.datetime.fromtimestamp(time.mktime(entry.published_parsed))
        now = datetime.datetime.now()
        
        date_str = published_dt.strftime("%d %b")
        
        if published_dt.date() == now.date():
            return f"Today, {date_str}"
        else:
            if published_dt.year == now.year:
                return date_str
            else:
                return published_dt.strftime("%d %b %Y")
    except:
        return f"Today, {datetime.datetime.now().strftime('%d %b')}"

def fetch_news_background():
    """
    Background worker to fetch news. Updates cache intermittently.
    No longer blocks server startup.
    """
    global NEWS_CACHE
    
    # On-demand fetch (Serverless friendly)
    if not NEWS_CACHE["data"] or time.time() - NEWS_CACHE["last_update"] > CACHE_DURATION:
        try:
            print(f"[NEWS] Fetching India Today RSS: {INDIA_TODAY_RSS}")
            import requests
            response = requests.get(INDIA_TODAY_RSS, timeout=12)
            if response.status_code == 200:
                import feedparser
                feed = feedparser.parse(response.content)
                if feed.entries:
                    news_items = []
                    for entry in feed.entries[:15]:
                        import re
                        summary = re.sub('<[^<]+?>', '', entry.summary) if hasattr(entry, 'summary') else ""
                        news_items.append({
                            "title": entry.title,
                            "link": entry.link,
                            "date": format_rss_date(entry),
                            "summary": summary[:200]
                        })
                    NEWS_CACHE["data"] = news_items
                    NEWS_CACHE["last_update"] = time.time()
                    top_title = news_items[0]['title'][:50] if news_items else "N/A"
                    print(f"[NEWS] Success! Cached {len(news_items)} items. Top: {top_title}...")
                else:
                    print("[NEWS] Warning: Feed entries list is empty.")
            else:
                print(f"[NEWS] Error: Feed returned status {response.status_code}")
        except Exception as e:
            print(f"[NEWS FETCH ERROR] {e}")

@app.route('/news', methods=['GET'])
def get_news():
    fetch_news_background()
    # Return cache immediately (non-blocking)
    # Fallback mock data if cache is totally empty on first boot
    mock_news = [
        {"title": "Syncing latest headlines from India Today...", "link": "#", "date": f"Today, {datetime.datetime.now().strftime('%d %b')}"},
        {"title": "MahaDBT Scholarship deadline extended to March 31st", "link": "#", "date": "16 Mar"}
    ]
    return jsonify(NEWS_CACHE["data"] if NEWS_CACHE["data"] else mock_news)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5002))
    app.run(host="0.0.0.0", port=port, debug=True)
