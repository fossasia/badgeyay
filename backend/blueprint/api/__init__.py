import os
from flask import Flask
import firebase_admin
from firebase_admin import credentials
from api.config import config
from flask_cors import CORS


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    cred = credentials.Certificate(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config', 'ServiceAccountkey.json'))
    firebase_admin.initialize_app(cred)
    app.config['BASE_DIR'] = os.path.dirname(os.path.abspath(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % config.POSTGRES
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SECRET_KEY'] = config.POSTGRES['secret']
    app.config['DEBUG'] = config.DEBUG
    app.config.from_object('api.config.mailConfig.MailConfig')
    CORS(app, resources={r"*": {"origins": "*"}})

    return app
