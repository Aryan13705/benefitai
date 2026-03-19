from backend.app import app as flask_app

def vercel_app(environ, start_response):
    path_info = environ.get("PATH_INFO", "")
    if path_info.startswith("/api"):
        # Strip the /api prefix, fallback to / if empty
        environ["PATH_INFO"] = path_info[4:] or "/"
    return flask_app(environ, start_response)

app = vercel_app
