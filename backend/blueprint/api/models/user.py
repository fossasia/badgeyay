from werkzeug.security import generate_password_hash
# from api.utils.mail import sendMail
from api.db import db


class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.String(100))
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(100))
    email = db.Column(db.String(100))
    files = db.relationship('File', backref='uploader')
    badges = db.relationship('Badges', backref='creator')

    def __init__(self, id_, username, password, email):
        self.id = id_
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email

    def save_to_db(self):
        db.session.add(self)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            print(e)

    @classmethod
    def getUser(cls, user_id=None, username=None):
        if username is None:
            return cls.query.filter_by(id=user_id).first()
        if user_id is None:
            return cls.query.filter_by(username=username).first()


# @db.event.listens_for(User, "after_insert")
# def sendVerification(mapper, connection, target):
#     msg = {}
#     msg['subject'] = "Welcome to Badgeyay"
#     msg['receipent'] = target.email
#     msg['body'] = "It's good to have you onboard with Badgeyay. Welcome to the" \
#         "FOSSASIA Family."
#     sendMail(msg)
