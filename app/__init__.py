import os
from flask import current_app
from flask_jwt_extended import JWTManager
from instance.config import Config
import datetime
from flask import Flask, Blueprint
from flask_cors import CORS
from instance.config import app_config
from app.api.v2.routes import version_two as v2
from db_config import Db
from flask import jsonify


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(v2)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config_name])
    CORS(app)
    JWTManager(app)

    return app
