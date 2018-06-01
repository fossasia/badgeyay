import os
from flask import Flask
import firebase_admin
from firebase_admin import credentials
from api.config import config
from flask_cors import CORS
from flask_migrate import Migrate
from api.db import db
from dotenv import load_dotenv, find_dotenv
from api.controllers import (
    generateBadges,
    homePage,
    errorHandlers,
    loginUser,
    fileUploader,
    modifyUser,
    resetUser,
    registerUser,
    oauthToken,
    assetHelper,
    admin
)


load_dotenv(find_dotenv())


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    cred = credentials.Certificate(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config', 'ServiceAccountkey.json'))
    firebase_admin.initialize_app(cred)
    app.config['BASE_DIR'] = os.path.dirname(os.path.abspath(__file__))
    if not config.DEBUG:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
    elif config.ENV == 'LOCAL':
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % config.POSTGRES
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['DEBUG'] = os.getenv('DEBUG')
    app.config.from_object('api.config.mailConfig.MailConfig')
    app.config.from_object(os.getenv('APP_CONFIG', default='api.config.config.ProductionConfig'))
    CORS(app, resources={r"*": {"origins": "*"}})
    db.init_app(app)
    Migrate(app, db)

    with app.app_context():
        app.register_blueprint(generateBadges.router, url_prefix='/api')
        app.register_blueprint(registerUser.router, url_prefix='/user')
        app.register_blueprint(loginUser.router, url_prefix='/user')
        app.register_blueprint(fileUploader.router, url_prefix='/api/upload')
        app.register_blueprint(modifyUser.router, url_prefix='/user/change')
        app.register_blueprint(homePage.router)
        app.register_blueprint(errorHandlers.router)
        app.register_blueprint(assetHelper.router, url_prefix='/api')
        app.register_blueprint(resetUser.router, url_prefix='/reset')
        app.register_blueprint(oauthToken.router, url_prefix='/api')
        app.register_blueprint(admin.router, url_prefix='/admin')

    return app
