import uuid
from api.db import db
import datetime


class Badges(db.Model):

    __tablename__ = 'Badges'

    @classmethod
    def _get_date(self):
        return datetime.datetime.now()

    badge_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id', ondelete='CASCADE'))
    logo = db.Column(db.String(100), nullable=False)
    background_image = db.Column(db.String(100), nullable=False)
    csv = db.Column(db.String(100), nullable=False)
    font = db.Column(db.String(100), nullable=False)
    font_size = db.Column(db.String(100), nullable=False)
    font_color = db.Column(db.String(100), nullable=False)
    badge_size = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.Date, default=_get_date)
    updated_at = db.Column(db.Date, onupdate=_get_date)

    def __init__(self, event_logo=None, background_image=None, csv=None, font=None, font_size=None, font_color=None, badge_size=None, creator=None):
        self.badge_id = str(uuid.uuid4())
        self.event_logo = event_logo
        self.background_image = background_image
        self.csv = csv
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.badge_size = badge_size
        self.creator = creator

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
