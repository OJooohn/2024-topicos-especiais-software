# codigo para criar o banco

from config import app, db
from models import User, Event

with app.app_context():
    db.create_all()  # precisa de um contexto

