from flask import Flask
from controllers import generateBadges
from controllers import homePage
from controllers import errorHandlers

app = Flask(__name__)


app.register_blueprint(generateBadges.router, url_prefix="/api")
app.register_blueprint(homePage.router)
app.register_blueprint(errorHandlers.router)


app.run()
