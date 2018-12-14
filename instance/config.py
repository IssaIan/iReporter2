import os
import datetime
class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    DB_HOST = os.getenv('DB_HOST')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(hours=12)
   

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    DB_NAME = os.getenv('DB_NAME')

class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True
    DB_NAME = os.getenv('DBTEST_NAME')

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False
    DB_NAME = os.getenv('DB_NAME')

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}

   
