from werkzeug.security import generate_password_hash

from api.utils.mail import sendMail
from api.db import db


class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(100))
    name = db.Column(db.String(80))

    def __init__(self, username, password, name):
        self.username = username
        self.password = generate_password_hash(password)
        self.name = name

    def save_to_db(self):
        db.session.add(self)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            print(e)

    @classmethod
    def getUser(cls, username):
        return cls.query.filter_by(username=username).first()


@db.event.listens_for(User, "after_insert")
def sendVerification(mapper, connection, target):
    msg = {}
    msg['subject'] = "Welcome to Badgeyay"
    msg['receipent'] = target.username
    msg['body'] = "It's good to have you onboard with Badgeyay. Welcome to " \
        "FOSSASIA Family."
    sendMail(msg)
