from flask_login import current_user

from ..models import Appointment
from .. import db
from ..utils import commit_after

class AppointmentService:
    @staticmethod
    @commit_after
    def create_appointment(pet_id, user_id, schedule):
        new_appointment = Appointment(pet_id=pet_id, user_id=user_id, schedule=schedule)
        db.session.add(new_appointment)
        return new_appointment
    
    def get_appointments(idx=None):
        if idx:
            rta = Appointment.query.filter_by(user_id = idx).all()
        else:
            rta = Appointment.query.all()
        return rta
