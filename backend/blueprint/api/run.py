import os
from db import db
from app import create_app
from controllers import generateBadges
from controllers import homePage
from controllers import errorHandlers
from controllers import registerUser
from controllers import loginUser
from controllers import fileUploader
from api.controllers import modifyUser


config_name = os.getenv('APP_SETTINGS')  # config_name = "development"
app = create_app(config_name)


app.register_blueprint(generateBadges.router, url_prefix='/api')
app.register_blueprint(registerUser.router, url_prefix='/user')
app.register_blueprint(loginUser.router, url_prefix='/user')
app.register_blueprint(fileUploader.router, url_prefix='/api/upload')
app.register_blueprint(modifyUser.router, url_prefix='/user/change')
app.register_blueprint(homePage.router)
app.register_blueprint(errorHandlers.router)


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    app.run()
