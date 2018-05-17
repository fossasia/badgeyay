from api.db import db


class File(db.Model):
    __tablename__ = 'File'

    filename = db.Column(db.String(100), NULLABLE=False)
    filetype = db.Coloumn(db.string(100), NULLABLE=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id', ondelete='CASCADE'))

    def __init__(self, filename, filetype):
        self.filename = filename
        self.filetype = filetype

    def save_to_db(self):
        db.session.add(self)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            print(e)

    def __repr__(self):
        return '<File: {}>'.format(self.name)
