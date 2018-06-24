from api.db import db


class UserPermission(db.Model):
    """
    Manage Permission of Users
    """
    __tablename__ = 'user_permissions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String)
    verified_user = db.Column(db.Boolean)
    anonymous_user = db.Column(db.Boolean)

    def __init__(self, name, description, verified_user=False, anonymous_user=False):
        self.name = name
        self.description = description
        self.verified_user = verified_user
        self.anonymous_user = anonymous_user

    def save_to_db(self):
        db.session.add(self)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            print(e)

    def __repr__(self):
        return '<UserPerm {}>'.format(self.name)

    def __str__(self):
        return self.__repr__()
