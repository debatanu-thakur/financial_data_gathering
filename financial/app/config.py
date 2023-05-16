
from .constants import DATABASE_URI

class Config(object):
    """Base config vars."""
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    


class ProdConfig(Config):
    DEBUG = False
    TESTING = False
    LOGIN_DISABLED = False

class DevConfig(Config):
    DEBUG = True
    TESTING = True
    LOGIN_DISABLED = False 