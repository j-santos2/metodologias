from .. import db

specialties = db.Table('specialties',
    db.Column('specialist_id', db.Integer, db.ForeignKey('specialist.id'), primary_key=True),
    db.Column('specialty_id', db.Integer, db.ForeignKey('specialty.id'), primary_key=True)
)

class Specialist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    specialties = db.relationship('specialties', secondary = specialties, lazy = 'subquery',
        backref = db.backref('specialist', lazy=True))

    def __repr__(self):
        return f'Specialist({self.id}, {self.name})'

class Specialty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    specialty = db.Column(db.String(200), unique=True, nullable=False)

    def __repr__(self):
        return f'Specialty({self.id}, {self.specialty})'
