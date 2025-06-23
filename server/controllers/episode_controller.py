from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from models.episode import Episode
from models import db

episode_bp = Blueprint("episode", __name__)

@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{"id": e.id, "date": e.date, "number": e.number} for e in episodes])

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    e = Episode.query.get_or_404(id)
    return jsonify({"id": e.id, "date": e.date, "number": e.number})

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    e = Episode.query.get_or_404(id)
    db.session.delete(e)
    db.session.commit()
    return jsonify(message="Deleted")
