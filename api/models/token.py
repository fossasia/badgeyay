from api.db import db


class ResetPasswordToken(db.Model):

    __tablename__ = 'Reset Password Token'

    id = db.Column(db.String, primary_key=True)
    token = db.Column(db.String, nullable=False)

    def __init__(self, uid, token):
        self.id = uid
        self.token = token

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            print(e)
