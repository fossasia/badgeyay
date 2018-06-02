from api.db import db
from api import create_app


app = create_app()


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    app.run()
