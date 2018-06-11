from werkzeug.security import generate_password_hash
from api.db import db


class Admin(db.Model):
    __tablename__ = 'Admin'

    id = db.Column(db.String(100), primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(100))
    email = db.Column(db.String(100))
    photoURL = db.Column(db.String())

    def __init__(self, id_, username, password, email, photoURL=None):
        self.id = id_
        self.username = username
        if password:
            self.password = generate_password_hash(password)
        self.email = email
        if photoURL:
            self.photoURL = photoURL
        else:
            self.photoURL = 'Some default asset'

    def save_to_db(self):
        db.session.add(self)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            print(e)

    @classmethod
    def getAdmin(cls, admin_id=None, username=None):
        if username is None:
            return cls.query.filter_by(id=admin_id).first()
        if admin_id is None:
            return cls.query.filter_by(username=username).first()
