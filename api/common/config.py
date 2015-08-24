__author__ = 'matti'
class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:testipassu@localhost/gachimuchio'

class DebugConfig(Config):
    DEBUG = True