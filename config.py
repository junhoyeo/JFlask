import os


class Config(object):
    SERVICE_NAME = 'Flask API'

    JWT_TOKEN_LOCATION = 'headers',
    JWT_HEADER_NAME = 'Authorization',
    JWT_HEADER_TYPE	= 'Bearer'


class DevConfig(Config):
    HOST = 'localhost'
    PORT = 5000
    DEBUG = True
