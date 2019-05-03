import datetime

from api.db import db
from api.config import config


class Settings(db.Model):

    __tablename__ = 'Settings'
    environment = ['Development', 'Production', 'Staging']

    id = db.Column(db.DateTime, default=datetime.datetime.utcnow, primary_key=True)
    appEnvironment = db.Column(db.Integer, nullable=False)
    appName = db.Column(db.String, default='Badgeyay', nullable=False)
    secretKey = db.Column(db.String, nullable=False)

    # Firebase config
    firebaseStorageBucket = db.Column(db.String, nullable=False)
    firebaseDatabaseURL = db.Column(db.String, nullable=False)

    # Email settings
    fromMail = db.Column(db.String, default="bagdeyayofficial@gmail.com")

    # Send Grid config
    sendGridApiKey = db.Column(db.String)

    def __init__(self,
                 appEnvironment,
                 appName,
                 secretKey,
                 firebaseDatabaseURL,
                 firebaseStorageBucket,
                 **kwargs):
        self.appEnvironment = appEnvironment
        self.appName = appName
        self.secretKey = secretKey
        self.firebaseStorageBucket = firebaseStorageBucket
        self.firebaseDatabaseURL = firebaseDatabaseURL
        if 'fromMail' in kwargs.keys():
            self.fromMail = kwargs['fromMail']
        if 'sendGridApiKey' in kwargs.keys():
            self.sendGridApiKey = kwargs['sendGridApiKey']

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            db.session.flush()

    @staticmethod
    def init_setup():
        if len(Settings.query.all()) == 0:
            settings = Settings(0,
                                'Badgeyay',
                                config.POSTGRES['secret'],
                                'https://badgeyay-195bf.firebaseio.com',
                                'badgeyay-195bf.appspot.com')
            settings.save_to_db()
        else:
            settings = Settings.latest_settings()
        return settings

    @staticmethod
    def latest_settings():
        return Settings.query.order_by(Settings.id.desc()).first()
