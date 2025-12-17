import os

class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    DEBUG = True
    SECRET_KEY = 'dev-secret-key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
