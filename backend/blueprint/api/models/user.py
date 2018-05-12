from werkzeug.security import generate_password_hash


from api.db import db


class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(100))
    name = db.Column(db.String(80))
    email = db.Column(db.String(100))

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = generate_password_hash(password)
        self.name = name
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
    def getUser(cls, username):
        return cls.query.filter_by(username=username).first()
