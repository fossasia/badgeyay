from api.db import db


class SocialContent(db.Model):
    __tablename__ = 'SocialContent'

    name = db.Column(db.String, primary_key=True)
    description = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False)
    icon = db.Column(db.String, nullable=False)  # Semantic ui class for the icon of media

    def __init__(self, name, description, link, icon):
        self.name = name.lower()
        self.description = description
        self.link = link
        self.icon = icon

    def save_to_db(self):
        db.session.add(self)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            print(e)

    @classmethod
    def populate_initial(cls):
        if not SocialContent.check_key('github'):
            db.session.add(SocialContent('github', 'Social network for developers', 'https://github.com/fossasia/badgeyay', 'github icon'))
            db.session.commit()
        if not SocialContent.check_key('twitter'):
            db.session.add(SocialContent('twitter', 'Online news and social networking service', 'https://twitter.com/badgeyay', 'twitter icon'))
            db.session.commit()

    @staticmethod
    def check_key(key):
        return SocialContent.query.filter_by(name=key.lower()).first()
