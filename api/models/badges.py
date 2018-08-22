from api.db import db
from datetime import datetime
import uuid


class Badges(db.Model):
    __tablename__ = 'Badges'

    id = db.Column(db.String(100), primary_key=True)
    image = db.Column(db.String(100), nullable=False)
    csv = db.Column(db.String(100), nullable=False)
    text_color = db.Column(db.String(100), nullable=False)
    badge_size = db.Column(db.String(100), nullable=False)
    download_link = db.Column(db.String)
    image_link = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)
    badge_name = db.Column(db.String(100), default='My Badge')
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

    def delete_from_db(self):
        self.deleted_at = datetime.utcnow()
        self.save_to_db()

    @classmethod
    def getBadge(cls, badge_id):
        return cls.query.filter_by(id=badge_id).first()
