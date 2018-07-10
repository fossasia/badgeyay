from werkzeug.security import generate_password_hash
from datetime import datetime
from api.db import db


def _photoURL():
    return 'https://encrypted-tbn0.gstatic.com/' \
        'images?q=tbn:ANd9GcRWnJC8FyOPb9J-EjhQStzIZt_dk-dxuK-VyEnwQDdqIBKj4p7R8A'


class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.String(100), primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(100))
    email = db.Column(db.String(100))
    photoURL = db.Column(db.String, default=_photoURL)
    allowed_usage = db.Column(db.Integer)
    ftl = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)
    files = db.relationship('File', backref='uploader')
    badges = db.relationship('Badges', backref='creator')
    permissions = db.relationship('Permissions', backref='user_permissions', lazy='dynamic')
    siteAdmin = db.Column(db.Boolean, default=False)

    def __init__(self, id_, username, password, email, photoURL=None):
        self.id = id_
        self.username = username
        self.allowed_usage = 200
        if password:
            self.password = generate_password_hash(password)
        self.email = email
        if photoURL:
            self.photoURL = photoURL

    def create_site_admin(self):
        self.siteAdmin = True
        self.save_to_db()

    def save_to_db(self):
        db.session.add(self)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            print(e)

    def delete_user(self):
        db.session.delete(self)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            print(e)

    @classmethod
    def getUser(cls, user_id=None, username=None, email=None):
        if user_id:
            return cls.query.filter_by(id=user_id).first()
        if username:
            return cls.query.filter_by(username=username).first()
        if email:
            return cls.query.filter_by(email=email).first()
