from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Game, Base
from faker import Faker
import random

# Initialize SQLAlchemy session
engine = create_engine('sqlite:///your_database_name.db')
Base.metadata.create_all(engine)  # Add this line to create tables

Session = sessionmaker(bind=engine)
session = Session()

# Clear existing data (optional but prevents duplicates)
session.query(Game).delete()
session.commit()

# Seed with Faker
fake = Faker()
games = [
    Game(
        title=fake.name(),
        genre=fake.word(),
        platform=fake.word(),
        price=random.randint(0, 60)
    )
    for _ in range(50)
]
session.add_all(games)
session.commit()
print("Seeding complete!")  # Confirm success