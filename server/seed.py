from models import db
from models.user import User
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance
from faker import Faker
import random
from datetime import datetime, timedelta
from app import app

fake = Faker()

with app.app_context():
    db.drop_all()
    db.create_all()

    users = []
    for _ in range(5):
        user = User(username=fake.user_name())
        user.set_password('password123')
        users.append(user)
        db.session.add(user)

    occupations = [
        'Actor', 'Actress', 'Musician', 'Singer', 'Comedian', 'Director', 
        'Producer', 'Writer', 'Scientist', 'Politician', 'Athlete', 
        'Chef', 'Artist', 'Entrepreneur', 'Author', 'Journalist'
    ]
    
    guests = []
    for _ in range(20):
        guest = Guest(name=fake.name(), occupation=random.choice(occupations))
        guests.append(guest)
        db.session.add(guest)

    episodes = []
    start_date = datetime.now() - timedelta(days=90)
    
    for i in range(15):
        episode_date = start_date + timedelta(days=i * 7)
        episode = Episode(date=episode_date.strftime('%Y-%m-%d'), number=i + 1)
        episodes.append(episode)
        db.session.add(episode)
    
    db.session.commit()
    
    appearances = []
    for _ in range(random.randint(10, 15)):
        appearance = Appearance(
            rating=random.randint(1, 5),
            guest_id=random.choice(guests).id,
            episode_id=random.choice(episodes).id
        )
        appearances.append(appearance)
        db.session.add(appearance)

    db.session.commit()


if __name__ == '__main__':
    print("Seeding complete.")
