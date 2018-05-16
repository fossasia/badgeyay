import os
import uuid

class Badges(db.Model):
    __tablename__ = 'Badges'

    image = db.Column(db.String(100), NULLABLE=False)
    csv = db.Column(db.String(100), NULLABLE=False)
    badge_id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('User.id', ondelete='CASCADE'))

    def __init__(self, fileName=None, imageName=None):
        self.image = imageName
        self.csv = csvName
        self.badge_id = str(uuid.uuid4())

    def save_to_db(self):
        db.session.add(self)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            print(e)

    @classmethod
    def getBadge(cls, badge_id):
        return cls.query.filter_by(badge_id=badge_id).first()
