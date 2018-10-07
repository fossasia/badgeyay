from api.db import db


class Stripe(db.Model):
    __tablename__ = 'Stripe'

    id = db.Column(db.Integer, primary_key=True)
    stripe_secret_key = db.Column(db.String)
    stripe_refresh_token = db.Column(db.String)
    stripe_publishable_key = db.Column(db.String)
    stripe_user_id = db.Column(db.String)
    stripe_auth_code = db.Column(db.String)
    amount = db.Column(db.String)
    currency = db.Column(db.String)

    def __init__(self,
                 stripe_secret_key=None,
                 stripe_refresh_token=None,
                 stripe_publishable_key=None,
                 stripe_user_id=None,
                 stripe_auth_code=None,
                 amount=None,
                 currency=None):
        self.stripe_secret_key = stripe_secret_key
        self.stripe_refresh_token = stripe_refresh_token
        self.stripe_publishable_key = stripe_publishable_key
        self.stripe_user_id = stripe_user_id
        self.stripe_auth_code = stripe_auth_code
        self.amount = amount
        self.currency = currency

    def save_to_db(self):
        db.session.add(self)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            print(e)
