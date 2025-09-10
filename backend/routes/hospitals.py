from flask import Blueprint, request, jsonify
from models import db, Hospital

hospital_bp = Blueprint("hospital", __name__)

@hospital_bp.route("/hospitals", methods=["GET"])
def get_hospitals():
    hospitals = Hospital.query.all()
    return jsonify([{
        "id": h.id, "name": h.name,
        "address": h.address, "specialization": h.specialization
    } for h in hospitals])

@hospital_bp.route("/hospitals", methods=["POST"])
def add_hospital():
    data = request.json
    hospital = Hospital(name=data["name"], address=data["address"], specialization=data["specialization"])
    db.session.add(hospital)
    db.session.commit()
    return jsonify({"message": "Hospital added"}), 201
