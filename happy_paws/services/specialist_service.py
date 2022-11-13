from ..models import Specialist, Specialty
from .. import db
from ..utils import commit_after


class SpecialistService:
    @staticmethod
    @commit_after
    def create_specialist(name, user_id, specialty_name):
        specialty = SpecialtyService.get_or_create(specialty_name)
        new_specialist = Specialist(name=name, user_id=user_id, specialty_id=specialty.id)
        db.session.add(new_specialist)
        return new_specialist
    

class SpecialtyService:
    @staticmethod
    @commit_after
    def create_specialty(specialty):
        new_specialty = Specialty(specialty=specialty)
        db.session.add(new_specialty)
        return new_specialty
         

    @staticmethod
    def get_or_create(specialty):
        result = Specialty.query.filter_by(specialty=specialty).first()
        if result is None:
            result = SpecialtyService.create_specialty(specialty)
        return result
