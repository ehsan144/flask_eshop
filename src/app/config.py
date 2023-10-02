from os import getenv as env, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))


class Config(object):
    load_dotenv()
    SQLALCHEMY_DATABASE_URI = env("DATABASE_URL")
    SECRET_KEY = env("SECRET_KEY")
    DEBUG = False
    TESTING = False
    POSTGRES_USER = "eshop"
    POSTGRES_PASSWORD = "123456"
    POSTGRES_DB = "eshop"
    POSTGRES_HOST = "db"


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
