from os import getenv as env, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))


class Config(object):
    load_dotenv()
    SQLALCHEMY_DATABASE_URI = env("DATABASE_URL")
    SECRET_KEY = env("SECRET_KEY")
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = env("PRO_DATABASE_URL", 'sqlite:///:memory:')


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = env("TEST_DATABASE_URL", 'sqlite:///:memory:')
    TESTING = True
