from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(1000))

# Id = primary key 
# title = samsung s23
# description = text description 
# Image = url
# Price = prices integer 
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    title = db.Column(db.String(255))
    description = db.Column(db.String(1000))
    image = db.Column(db.String(255))
    price = db.Column(db.Integer)