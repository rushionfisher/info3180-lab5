# Add any model classes for Flask-SQLAlchemy here
from . import db
from datetime import datetime

class Movie(db.Model):
    __tablename__= 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    poster = db.Column(db.String(255), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, title, description, poster):
        self.title = title
        self.description = description
        self.poster = poster