from api.db import db
from datetime import datetime


class Roles(db.Model):

    __tablename__ = 'Roles'

    name = db.Column(db.String, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)
    isDefault = db.Column(db.Boolean, default=True)

    def __init__(self, name, isDefault):
        self.name = name.lower()
        self.isDefault = isDefault

    def deleteRole(self, deleted_at):
        self.deleted_at = deleted_at

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            print(e)
