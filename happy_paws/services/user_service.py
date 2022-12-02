from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash

from .appointment_service import AppointmentService
from .pet_service import PetService
from ..models import User
from .. import db
from ..utils import commit_after

class ROLE:
    default = 0
    admin = 1

class UserService:
    @staticmethod
    @commit_after
    def create_user(email, username, password, role=ROLE.default):
        hashed_pass = generate_password_hash(password)
        new_user = User(email=email, username=username, password=hashed_pass, role=role)
        db.session.add(new_user)
        return new_user
    
    @staticmethod
    def authenticate(username, password):
        if username:
            user = User.query.filter_by(username=username).first()
            if user and check_password_hash(user.password, password):
                login_user(user)
                return True
        return False

    @staticmethod
    def get_user_pets(user_id):
        return PetService.get_pets_by_user(user_id)

    @staticmethod
    def get_user_appointments(user_id):
        return AppointmentService.get_appointments(user_id)
