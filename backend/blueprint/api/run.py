from flask import Flask
from config import config
from db import db
from controllers import generateBadges
from controllers import homePage
from controllers import errorHandlers
from controllers import registerUser
from controllers import loginUser


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % config.POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = config.POSTGRES['secret']


app.register_blueprint(generateBadges.router, url_prefix='/api')
app.register_blueprint(registerUser.router, url_prefix='/user')
app.register_blueprint(loginUser.router, url_prefix='/user')
app.register_blueprint(homePage.router)
app.register_blueprint(errorHandlers.router)


@app.before_first_request
def create_tables():
    db.create_all()


db.init_app(app)
app.run(debug=True)
