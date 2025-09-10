from flask import Blueprint, request, jsonify
from models import db, Doctor

doctor_bp = Blueprint("doctor", __name__)

@doctor_bp.route("/doctors/<int:hospital_id>", methods=["GET"])
def get_doctors(hospital_id):
    doctors = Doctor.query.filter_by(hospital_id=hospital_id).all()
    return jsonify([{
        "id": d.id, "name": d.name, "specialization": d.specialization, "timings": d.timings
    } for d in doctors])

@doctor_bp.route("/doctors", methods=["POST"])
def add_doctor():
    data = request.json
    doctor = Doctor(
        name=data["name"],
        specialization=data["specialization"],
        hospital_id=data["hospital_id"],
        timings=data["timings"]
    )
    db.session.add(doctor)
    db.session.commit()
    return jsonify({"message": "Doctor added"}), 201
