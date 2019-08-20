import os
from flask import Flask
import firebase_admin
from firebase_admin import credentials
from backend.config import config
from flask_cors import CORS
from backend.models.settings import Settings
from backend.db import db
from backend.utils.dimen import init_dimen


def create_app():
    app = Flask(__name__, instance_relative_config=True, static_folder='static')
    cred = credentials.Certificate(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config', 'ServiceAccountkey.json'))
    app.config['BASE_DIR'] = os.path.dirname(os.path.abspath(__file__))
    if not config.DEBUG:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
    elif config.ENV == 'LOCAL':
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % config.POSTGRES
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    init_dimen()

    with app.app_context():
        db.init_app(app)
        db.create_all()
        settings = Settings.init_setup()
        firebase_admin.initialize_app(cred, {
            'storageBucket': settings.firebaseStorageBucket,
            'databaseURL': settings.firebaseDatabaseURL
        })
    app.config['SECRET_KEY'] = settings.secretKey
    if Settings.environment[settings.appEnvironment] == 'Development':
        app.config['DEBUG'] = True
    else:
        app.config['DEBUG'] = False
    app.config["POSTS_PER_PAGE"] = config.POSTS_PER_PAGE
    CORS(app, resources={r"*": {"origins": "*"}})

    return app
