from app import db
from datetime import datetime

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(70), unique=True, nullable=False)
    pizzas = db.relationship('Restaurant_pizza', backref='restaurant', lazy=True)

class Pizzas(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    ingredients = db.Column(db.String(50), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Set the default value to the current timestamp
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)  # Set the default value to the current timestamp and update on each update
    restaurants = db.relationship('Restaurant_pizza', backref='pizza', lazy=True)

class Restaurant_pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Set the default value to the current timestamp
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)  # Set the default value to the current timestamp and update on each update
