from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import db, User
from utils import hash_password, verify_password

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "Email already exists"}), 400
    user = User(
        name=data["name"],
        email=data["email"],
        password=hash_password(data["password"]),
        role=data.get("role", "patient")
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()
    if user and verify_password(data["password"], user.password):
        token = create_access_token(identity={"id": user.id, "role": user.role})
        return jsonify({"access_token": token, "role": user.role})
    return jsonify({"error": "Invalid credentials"}), 401
