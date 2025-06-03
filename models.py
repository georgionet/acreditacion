from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    special = db.Column(db.Boolean, default=False)
    special_reason = db.Column(db.String(255))
    accredited_at = db.Column(db.DateTime)
    accredited_by = db.Column(db.String(100))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
