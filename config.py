import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-change-this")

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB

    UPLOAD_FOLDER = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        "uploads",
        "invoices"
    )

    ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg"}