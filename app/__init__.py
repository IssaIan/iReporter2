from flask import Flask, Blueprint
from instance.config import app_config
from db_config import *
from .api.v1 import version_two as v2

def create_app(config_name='testing'):
    app = Flask(__name__, instance_relative_config=True)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config['testing'])
    app.config.from_pyfile('config.py')
    create_tables()
    app.register_blueprint(v2)
    return app

