from db import db
from werkzeug.security import generate_password_hash


class User(db.Model):
    __tablename__ = 'User'

    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(80))

    def __init__(self, username, password, name):
        self.username = username
        self.password = generate_password_hash(password)
        self.name = name

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def getUser(cls, username):
        return cls.query.filter_by(username=username).first()
