from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Ticket, User

ticket_bp = Blueprint("ticket", __name__)

@ticket_bp.route("/tickets", methods=["POST"])
@jwt_required()
def create_ticket():
    data = request.json
    identity = get_jwt_identity()
    patient_id = identity.get("id")
    ticket = Ticket(patient_id=patient_id, doctor_id=data["doctor_id"])
    db.session.add(ticket)
    db.session.commit()
    return jsonify({"message": "Ticket created", "ticket_id": ticket.id}), 201

@ticket_bp.route("/tickets/mine", methods=["GET"])
@jwt_required()
def get_my_tickets():
    identity = get_jwt_identity()
    patient_id = identity.get("id")
    tickets = Ticket.query.filter_by(patient_id=patient_id).all()
    return jsonify([{
        "id": t.id,
        "token_number": t.id,
        "status": t.status,
        "estimated_wait_minutes": None
    } for t in tickets])

@ticket_bp.route("/doctor/<int:doctor_id>/tokens", methods=["GET"])
@jwt_required()
def get_tokens(doctor_id):
    tickets = Ticket.query.filter_by(doctor_id=doctor_id, status="waiting").all()
    return jsonify([{
        "id": t.id,
        "patient_id": t.patient_id,
        "status": t.status,
        "token_number": t.id
    } for t in tickets])

@ticket_bp.route("/tickets/<int:ticket_id>/status", methods=["PUT"])
@jwt_required()
def update_status(ticket_id):
    data = request.json
    ticket = Ticket.query.get(ticket_id)
    if not ticket:
        return jsonify({"error": "Ticket not found"}), 404
    ticket.status = data["status"]
    db.session.commit()
    return jsonify({"message": "Ticket status updated"})
