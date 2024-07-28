from app import db
from datetime import datetime

class FAQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    answer = db.Column(db.String(500), nullable=False)

class Interaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_query = db.Column(db.String(200), nullable=False)
    bot_response = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
