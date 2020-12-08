from backend.db import db

class Module(db.Model):
    __tablename__ = 'Modules'

    id = db.Column(db.Integer, primary_key=True)
    ticketInclude = db.Column(db.Boolean, default=False)
    paymentInclude = db.Column(db.Boolean, default=False)
    donationInclude = db.Column(db.Boolean, default=False)

    def __init__(self, ticketInclude=True, paymentInclude=True, donationInclude=True):
        self.id = 1
        self.donationInclude = donationInclude
        self.paymentInclude = paymentInclude
        self.ticketInclude = ticketInclude

    @classmethod
    def set_default(cls):
        if len(Module.query.filter_by(id=1).all()) == 0:
            db.session.add(Module())
            db.session.commit()
        else:
            print('Module already created')

    def save_to_db(self):
        db.session.add(self)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            print(e)
