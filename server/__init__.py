from flask import Flask
from flask_common import Common
from flask_cors import CORS
from flask_principal import Principal
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
import os

from config import DevConfig
from server.namespaces import api


def create_app():
    _app = Flask(__name__)
    
    CORS().init_app(_app)
    Principal().init_app(_app)
    JWTManager().init_app(_app)
    _app.secret_key = os.urandom(24)
    _app.config.from_object(DevConfig)
    return _app


app = create_app()
api.init_app(app)
common = Common(app)
mongo = PyMongo(app)
