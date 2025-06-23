from server.models import db
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.app import app

with app.app_context():
    db.create_all()
    g1 = Guest(name="Tom Hanks", occupation="Actor")
    e1 = Episode(date="2025-01-01", number=1)
    db.session.add_all([g1, e1])
    db.session.commit()
    a1 = Appearance(rating=5, guest_id=g1.id, episode_id=e1.id)
    db.session.add(a1)
    db.session.commit()
