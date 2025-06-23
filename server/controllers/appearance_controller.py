from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models import db
from server.models.appearance import Appearance

bp = Blueprint("appearance", __name__)

@bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    if not (1 <= data['rating'] <= 5):
        return jsonify(error="Rating must be 1-5"), 400
    appearance = Appearance(**data)
    db.session.add(appearance)
    db.session.commit()
    return jsonify(message="Appearance created"), 201
