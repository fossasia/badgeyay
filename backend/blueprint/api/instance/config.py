import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


DEBUG = os.getenv('DEBUG')

POSTGRES = {
    'user': os.getenv('POSTGRES_USER'),
    'pw': os.getenv('POSTGRES_PASSWORD'),
    'host': os.getenv('POSTGRES_HOST'),
    'port': os.getenv('POSTGRES_PORT'),
    'db': os.getenv('POSTGRES_DATABASE'),
    'secret': os.getenv('POSTGRES_SECRET')
}


class MailConfig(object):
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT')
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS')
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')

class SwaggerConfig(object):
    SWAGGER = {
        "swagger": "3.0",
        "title": "Badgeyay Documentation",
        "description": "An API which genrates printable badges in a PDF",
        'uiversion': 3,
        "headers": [
            ('Access-Control-Allow-Origin', '*'),
            ('Access-Control-Allow-Methods', "GET, POST, PUT, DELETE, OPTIONS"),
            ('Access-Control-Allow-Credentials', "true"),
        ],
        "version": "1.0.1",
        "contact": {
            "responsibleOrganization": "FOSSASIA",
            "responsibleDeveloper": "FOSSASIA",
            "email": "fossasia@googlegroups.com",
            "url": "https://fossasia.org/",
        },
        "schemes": [
            "http",
            "https"
        ],
        "consumes": [
            "application/json",
        ],
        "produces": [
            "application/json",
        ],
    }

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/test_database'
    DEBUG = True


class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
