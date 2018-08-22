import uuid
from api.db import db


class File(db.Model):
    __tablename__ = 'File'

    id = db.Column(db.String(100))
    filename = db.Column(db.String(100), nullable=False, primary_key=True)
    filetype = db.Column(db.String(100), nullable=False)
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
