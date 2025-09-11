from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default="patient")  # patient, doctor, admin

class Hospital(db.Model):
    __tablename__ = "hospitals"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    address = db.Column(db.String(200))
    specialization = db.Column(db.String(100))

class Doctor(db.Model):
    __tablename__ = "doctors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    specialization = db.Column(db.String(100))
    hospital_id = db.Column(db.Integer, db.ForeignKey("hospitals.id"))
    timings = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True)

class Ticket(db.Model):
    __tablename__ = "tickets"
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctors.id"))
    status = db.Column(db.String(20), default="waiting")  # waiting, served, missed, cancelled
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
