from flask_login import UserMixin

from .. import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True, nullable=False)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.Integer, nullable=False, default=0)
    pets = db.relationship('Pet', backref='user', lazy=True)
    
    def __repr__(self):
        return f'User({self.id}, {self.email}, {self.username}, {self.role})'