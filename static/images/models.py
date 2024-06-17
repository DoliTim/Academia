from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class ZdravstveniDelavci(db.Model):
    __tablename__ = 'doctors'
    doctor_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

class Osebe(db.Model):
    __tablename__ = 'osebe'
    patient_id = db.Column(db.Integer, primary_key=True)
    health_in_number = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

class Zdravila(db.Model):
    __tablename__ = 'zdravila'
    Zdravila_id = db.Column(db.Integer, primary_key=True)
    Zdravilo = db.Column(db.String(255), nullable=False)

class Recepti(db.Model):
    __tablename__ = 'recepti'
    Recepti_id = db.Column(db.Integer, primary_key=True)
    Datum_izdaje = db.Column(db.DateTime, nullable=False, default=datetime.now)  # Use DateTime for timest
