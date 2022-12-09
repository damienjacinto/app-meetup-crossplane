from flask_sqlalchemy import SQLAlchemy
from database import db
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class DateCalender(db.Model):
    id = db.Column(db.String, unique=True, nullable=False, primary_key=True, default=generate_uuid)
    date = db.Column(db.Integer, unique=True, nullable=False)

    def __init__(self, id, date):
        self.id = id
        self.date = date

    def __init__(self, date):
        self.id = None
        self.date = date

    def __repr__(self):
        return f"<id={self.id}, date={self.date}>"