import os
from flask import Flask
import firebase_admin
from firebase_admin import credentials
from api.config import config
from flask_cors import CORS


def create_app():
    app = Flask(__name__, instance_relative_config=True, static_folder='static')
    cred = credentials.Certificate(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config', 'ServiceAccountkey.json'))
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'badgeyay-195bf.appspot.com'
    })
    app.config['BASE_DIR'] = os.path.dirname(os.path.abspath(__file__))
    if not config.DEBUG:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
    elif config.ENV == 'LOCAL':
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % config.POSTGRES
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SECRET_KEY'] = config.POSTGRES['secret']
    app.config['DEBUG'] = config.DEBUG
    app.config["POSTS_PER_PAGE"] = config.POSTS_PER_PAGE
    CORS(app, resources={r"*": {"origins": "*"}})

    return app
