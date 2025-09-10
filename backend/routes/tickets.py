from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Ticket, User

ticket_bp = Blueprint("ticket", __name__)

# ------------------- Patient: Create Ticket -------------------
@ticket_bp.route("/tickets", methods=["POST"])
@jwt_required()
def create_ticket():
    data = request.json
    identity = get_jwt_identity()
    patient_id = identity.get("id")

    ticket = Ticket(patient_id=patient_id, doctor_id=data["doctor_id"], status="waiting")
    db.session.add(ticket)
    db.session.commit()

    return jsonify({
        "message": "Ticket created",
        "ticket_id": ticket.id,
        "status": ticket.status
    }), 201


# ------------------- Patient: My Tickets -------------------
@ticket_bp.route("/tickets/mine", methods=["GET"])
@jwt_required()
def get_my_tickets():
    identity = get_jwt_identity()
    patient_id = identity.get("id")
    tickets = Ticket.query.filter_by(patient_id=patient_id).all()

    result = []
    for t in tickets:
        # Calculate how many tickets are ahead
        ahead_count = Ticket.query.filter(
            Ticket.doctor_id == t.doctor_id,
            Ticket.id < t.id,
            Ticket.status == "waiting"
        ).count()

        estimated_wait = ahead_count * 5  # assume 5 mins per patient

        result.append({
            "id": t.id,
            "token_number": t.id,
            "status": t.status,
            "estimated_wait_minutes": estimated_wait,
            "doctor_id": t.doctor_id
        })

    return jsonify(result)


# ------------------- Doctor: Get Tokens -------------------
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


# ------------------- Staff/Doctor: Update Status -------------------
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


# ------------------- Public: Queue Status -------------------
@ticket_bp.route("/queue/<int:doctor_id>", methods=["GET"])
def queue_status(doctor_id):
    # Find first waiting ticket
    now_serving = Ticket.query.filter_by(doctor_id=doctor_id, status="waiting") \
        .order_by(Ticket.id.asc()).first()

    waiting_count = Ticket.query.filter_by(doctor_id=doctor_id, status="waiting").count()
    avg_wait = waiting_count * 5  # assume 5 mins per patient

    return jsonify({
        "doctor_id": doctor_id,
        "now_serving": now_serving.id if now_serving else None,
        "waiting_count": waiting_count,
        "average_wait_time": avg_wait
    })
