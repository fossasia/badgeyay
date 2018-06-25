import uuid
from api.db import db


class Utilities(db.Model):
    __tablename__ = 'Utilities'

    id = db.Column(db.String(100), primary_key=True)
    pricing = db.Column(db.Float)

    def save_to_db(self):
        self.id = str(uuid.uuid4())
        db.session.add(self)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            print(e)
