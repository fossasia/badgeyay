import os

from api.db import db
from api.helpers.uploads.saveToImage import imageDirectory, imageName
from api.helpers.uploads.saveToCSV import csvDirectory, csvName


class File(db.Model):
    __tablename__ = 'File'

    image = db.Column(db.String(100), NULLABLE=False)
    csv = db.Coloumn(db.string(100), NULLABLE=False)

    user_id = db.Column(db.Integer, db.ForeignKey('User.id', ondelete='CASCADE'))

    def __init__(self, image, csv):
        self.image = os.path.join(imageDirectory, imageName)
        self.csv = os.path.join(csvDirectory, csvName)

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
