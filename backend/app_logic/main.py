from firebase_functions import https_fn
from firebase_admin import initialize_app
from app import app

initialize_app()

@https_fn.on_request()
def benefitai_api(req: https_fn.Request) -> https_fn.Response:
    return app
