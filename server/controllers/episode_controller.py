from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.episode import Episode
from server.models import db

bp = Blueprint("episode", __name__)

@bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{"id": e.id, "date": e.date, "number": e.number} for e in episodes])

@bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    e = Episode.query.get_or_404(id)
    return jsonify({"id": e.id, "date": e.date, "number": e.number})

@bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    e = Episode.query.get_or_404(id)
    db.session.delete(e)
    db.session.commit()
    return jsonify(message="Deleted")
