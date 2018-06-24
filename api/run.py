from flask_migrate import Migrate
from api import create_app
from api.db import db
from api.controllers import (
    generateBadges,
    errorHandlers,
    loginUser,
    fileUploader,
    modifyUser,
    resetUser,
    registerUser,
    oauthToken,
    assetHelper,
    updateProfile,
    admin,
    validation,
    changeMeta
)


app = create_app()


db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(generateBadges.router, url_prefix='/api')
app.register_blueprint(registerUser.router, url_prefix='/user')
app.register_blueprint(loginUser.router, url_prefix='/user')
app.register_blueprint(fileUploader.router, url_prefix='/api/upload')
app.register_blueprint(modifyUser.router, url_prefix='/user/change')
app.register_blueprint(errorHandlers.router)
app.register_blueprint(assetHelper.router, url_prefix='/api')
app.register_blueprint(resetUser.router, url_prefix='/reset')
app.register_blueprint(oauthToken.router, url_prefix='/api')
app.register_blueprint(admin.router, url_prefix='/admin')
app.register_blueprint(updateProfile.router, url_prefix='/update')
app.register_blueprint(validation.router, url_prefix='/validate')
app.register_blueprint(changeMeta.router, url_prefix='/change')


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    app.run()
