"""
The config defines system wide variables that have defaults in place but can
be overwritten by providing environment variables.
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))

# must provide the env var for postgres db
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL") or f"sqlite:///exam_api.db"
SECRET_KEY = os.getenv("SECRET_KEY", "completely_unsafe_dev_key")
