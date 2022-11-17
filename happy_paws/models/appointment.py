from datetime import datetime

from .. import db


class SpecialistMock:
    id = 1
    name = 'Jose'

class SpecialtyMock:
    name = 'Baño'


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    specialist = db.Column(db.String, default=SpecialistMock().name)
    specialty = db.Column(db.String, default=SpecialtyMock().name)
    schedule = db.Column(db.DateTime, nullable=False, default=datetime.now())
    state = db.Column(db.String, nullable=False, default='Pendiente')

    def __repr__(self):
        return f'Appointment(id:{self.id}, pet_id:{self.pet_id}, {self.user_id}, {self.specialist}, {self.specialty}, {self.schedule})'
