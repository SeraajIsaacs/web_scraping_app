from dotenv import load_dotenv
import os

# Configure the path to the SQLite database
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'instance', 'web_scraping_app.db')}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
load_dotenv()  # Load environment variables from .env file

class Config:
    SECRET_KEY = os.urandom(24)  # Randomly generated secret key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///web_scraping_app.db'  # SQLite database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')  # Get from .env
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')  # Get from .env
