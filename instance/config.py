import os
import datetime
class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(hours=12)
    UPLOAD_FOLDER = "upload"

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    DATABASE_URL = os.getenv('DATABASE_URL')

class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True
    DATABASE_URL = os.getenv('TESTDATABASE_URL')

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False
    DATABASE_URL = os.getenv('DATABASE_URL')

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

   
