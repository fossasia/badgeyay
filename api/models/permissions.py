from api.db import db
import uuid


class Permissions(db.Model):
    __tablename__ = 'Permissions'

    id = db.Column(db.String(100), primary_key=True)
    isUser = db.Column(db.Boolean, default=False)
    isAdmin = db.Column(db.Boolean, default=False)
    isSales = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.String(100), db.ForeignKey('User.id', ondelete='CASCADE'))

    def save_to_db(self):
        self.id = str(uuid.uuid4())
        db.session.add(self)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            print(e)

    @classmethod
    def getPermissions(cls, permissions_id):
        return cls.query.filter_by(user_id=permissions_id).first()
