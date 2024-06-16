from app.user.models import User, db
from app import create_app
from faker import Faker

fake = Faker('ka_GE')
app = create_app()

def create_users():
    with app.app_context():
        users = [User(username=fake.first_name(), email=fake.email(), password='123123')
                 for _ in range(200)]
        db.session.add_all(users)
        db.session.commit()


create_users()