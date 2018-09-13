# ---------------------------------------------------------------------------------
# Base App Configuration Class
# ---------------------------------------------------------------------------------
# BaseConfig is the base class used to set the configuration variables for
# all other development environments
#

class Config(object):
    ENV = 'this-really-needs-to-be-changed'
    DEVELOPMENT = False
    DEBUG = False
    SECRET_KEY = 'f96bb602022b917fe87fd5d2dcfe2ba0f6b2975d684adaee'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'this-really-needs-to-be-changed'


# ---------------------------------------------------------------------------------
# Production Configuration
# ---------------------------------------------------------------------------------
# ProductionConfig is the class used to set the appropriate configuration
# variables for the app in production
#

class ProductionConfig(Config):
    ENV = 'production'
    DEVELOPMENT = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'this-really-needs-to-be-changed'


# ---------------------------------------------------------------------------------
# Staging Configuration
# ---------------------------------------------------------------------------------
# StagingConfig is the class used to set the appropriate configuration
# variables for the app in staging
#

class StagingConfig(Config):
    ENV = 'development'
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'this-really-needs-to-be-changed'


# ---------------------------------------------------------------------------------
# Development Configuration
# ---------------------------------------------------------------------------------
# DevelopmentConfig is the class used to set the appropriate configuration
# variables for the app in development
#

class DevelopmentConfig(Config):
    ENV = 'development'
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'this-really-needs-to-be-changed'


# ---------------------------------------------------------------------------------
# Localhost Configuration
# ---------------------------------------------------------------------------------
# DevelopmentConfig is the class used to set the appropriate configuration
# variables for the app in local development
#

class LocalhostConfig(Config):
    ENV = 'development'
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://postgres:34fC$Q8BdsaXAuq&@db/flaskapp_db'
