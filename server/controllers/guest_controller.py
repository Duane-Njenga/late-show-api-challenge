from flask import Blueprint, jsonify
from server.models.guest import Guest

bp = Blueprint("guest", __name__)

@bp.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([{"id": g.id, "name": g.name, "occupation": g.occupation} for g in guests])
