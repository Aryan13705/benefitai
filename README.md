# BenefitAI — Frontend

Static HTML/CSS/JS pages. No build step required. Each page talks to the **backend** (Flask) via `fetch()`.

## Structure

```
frontend/
├── index.html           ← Home page
├── login.html           ← Login (email / Google / phone)
├── register.html        ← Registration with OTP
├── analyze.html         ← Profile analysis form
├── results.html         ← Scheme match results
├── dashboard.html       ← User dashboard (saved schemes)
├── profile_setup.html   ← Profile completion
├── css/
│   └── style.css
└── js/
    ├── api.js           ← API_BASE, apiFetch(), logActivity()
    └── auth.js          ← Firebase init + syncWithBackend()
```

## Running Locally

Make sure the backend is running first (port 5002), then serve the frontend:

```bash
cd frontend
python3 -m http.server 3000
```

Open **http://localhost:3000** in your browser.

> **Alternatively** — open any `.html` file directly in your browser. The backend CORS config allows `null` origin (file:// protocol) for local development.

## Configuration

The backend URL is set in `js/api.js`:

```js
const API_BASE = "http://127.0.0.1:5002";
```

Change this to your deployed backend URL when going to production.
