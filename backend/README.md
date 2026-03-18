# BenefitAI — Backend

Pure Flask REST API (JSON only). All HTML rendering happens in the `../frontend/` directory.

## Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Server runs on **http://127.0.0.1:5002**

## Key API Endpoints

| Method | Path | Auth Required | Description |
|--------|------|---------------|-------------|
| GET | `/` | No | Status / auth check |
| POST | `/register` | No | Register with email |
| POST | `/login` | No | Login with email + password |
| POST | `/firebase-login` | No | Login / register via Firebase |
| GET | `/me` | Yes | Get current user info |
| POST | `/complete-profile` | Yes | Save profile details |
| GET | `/dashboard` | Yes | Get saved schemes |
| POST | `/analyze` | No | Match schemes to profile |
| POST | `/save_scheme` | Yes | Save a scheme |
| POST | `/delete_scheme` | Yes | Remove a saved scheme |
| POST | `/send-otp` | No | Send email OTP (mock) |
| POST | `/verify-otp` | No | Verify email OTP |
| GET | `/get-universities` | No | Universities by state |
| POST | `/set-location` | No | Set state/university in session |
| POST | `/logout` | Yes | Log out |
| POST | `/log-activity` | No | Activity logging |

## Notes
- Sessions use `SameSite=None; Secure` in production — set `SESSION_COOKIE_SAMESITE` and `SESSION_COOKIE_SECURE`.
- Firebase Admin SDK key goes in `backend/firebase-adminsdk.json` (gitignored).
- Database: `schemes.db` (SQLite) — run `init_auth_db.py` to initialise.
