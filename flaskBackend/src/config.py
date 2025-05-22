# src/config.py
# from alembic import env
# from alembic.env import url


class Config:
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres@postgres:5432/base_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
