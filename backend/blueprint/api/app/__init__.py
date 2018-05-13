import os
from flask import Flask
from flask_migrate import Migrate
from db import db

# local import
from instance.config import app_config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config['BASE_DIR'] = os.path.dirname(os.path.abspath(__file__))
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config.from_object('instance.config.MailConfig')
    app.config.from_object('instance.config.SwaggerConfig')
    db.init_app(app)
    Migrate(app, db)

    return app
