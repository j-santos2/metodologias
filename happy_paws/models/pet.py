from .. import db


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    breed_id = db.Column(db.Integer, db.ForeignKey('breed.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'Pet({self.id}, {self.name}, {self.user_id}, {self.breed_id})'

class Breed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    breed = db.Column(db.String(200), unique=True, nullable=False)
    pets = db.relationship('Pet', backref='breed', lazy=True)

    def __repr__(self):
        return f'Breed({self.id}, {self.breed})'
