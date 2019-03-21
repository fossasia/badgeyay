from api.db import db
from datetime import datetime
import uuid


class Badges(db.Model):
    __tablename__ = 'Badges'

    id = db.Column(db.String(100), primary_key=True)
    image = db.Column(db.String, nullable=False)
    csv = db.Column(db.String(100), nullable=False)
    csv_type = db.Column(db.String(100), nullable=False)
    ticket_types = db.Column(db.String, nullable=False)
    badge_size = db.Column(db.String(100), nullable=False)
    download_link = db.Column(db.String)
    image_link = db.Column(db.String)
    logo_image_link = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)
    badge_name = db.Column(db.String(100), default='My Badge')
    user_id = db.Column(db.String(100), db.ForeignKey('User.id', ondelete='CASCADE'))
    logo_text = db.Column(db.String)
    logo_color = db.Column(db.String)
    logo_image = db.Column(db.String)
    font_color_1 = db.Column(db.String(100), nullable=False)
    font_color_2 = db.Column(db.String(100), nullable=False)
    font_color_3 = db.Column(db.String(100), nullable=False)
    font_color_4 = db.Column(db.String(100), nullable=False)
    font_color_5 = db.Column(db.String(100), nullable=False)
    font_size_1 = db.Column(db.String)
    font_size_2 = db.Column(db.String)
    font_size_3 = db.Column(db.String)
    font_size_4 = db.Column(db.String)
    font_size_5 = db.Column(db.String)
    font_type_1 = db.Column(db.String(100), nullable=False)
    font_type_2 = db.Column(db.String(100), nullable=False)
    font_type_3 = db.Column(db.String(100), nullable=False)
    font_type_4 = db.Column(db.String(100), nullable=False)
    font_type_5 = db.Column(db.String(100), nullable=False)
    paper_size = db.Column(db.String(100), nullable=False)
    download_link = db.Column(db.String)

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
        return cls.query.filter_by(id=badge_id)
