import os
from flask import Flask
from flask_migrate import Migrate
from api.db import db
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['BASE_DIR'] = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    app.config.from_object(os.getenv('APP_CONFIG', default='api.config.config.ProductionConfig'))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config.from_object('api.config.mailConfig.MailConfig')
    db.init_app(app)
    Migrate(app, db)

    return app
