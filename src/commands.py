from main import db
from flask import Blueprint

db_commands = Blueprint("db-custom", __name__)


@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables Created")


@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables Deleted")


@db_commands.cli.command("seed")
def seed_db():
    from models.Budget import Budget
    from models.User import User
    from main import bcrypt
    from faker import Faker
    import random

    faker = Faker()
    users = []

    for i in range(5):
        user = User()
        user.username = f"tester{i}"
        user.email = f"test{i}@test.com"
        user.password = bcrypt.generate_password_hash("123456").decode("utf-8")
        db.session.add(user)
        users.append(user)

    db.session.commit()

    for i in range(10):
        budget = Budget()
        budget.name = faker.catch_phrase()
        budget.user_id = random.choice(users).id
        db.session.add(budget)

    db.session.commit()
    print("Tables seeded")
