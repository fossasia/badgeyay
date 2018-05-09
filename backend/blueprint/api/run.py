import os
from flask import Flask
from flask_migrate import Migrate

from api.db import db
from api.config import config
from api.controllers import generateBadges
from api.controllers import homePage
from api.controllers import errorHandlers
from api.controllers import registerUser
from api.controllers import loginUser

app = Flask(__name__)
app.config['BASE_DIR'] = os.path.dirname(os.path.abspath(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % config.POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = config.POSTGRES['secret']
app.config['DEBUG'] = config.DEBUG

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(generateBadges.router, url_prefix='/api')
app.register_blueprint(registerUser.router, url_prefix='/user')
app.register_blueprint(loginUser.router, url_prefix='/user')
app.register_blueprint(fileUploader.router, url_prefix='/api/upload')
app.register_blueprint(homePage.router)
app.register_blueprint(errorHandlers.router)

@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    app.run()
