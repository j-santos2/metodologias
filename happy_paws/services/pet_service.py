from ..models import Pet, Breed
from .. import db
from ..utils import commit_after


class PetService:
    @staticmethod
    @commit_after
    def create_pet(name, user_id, breed_name):
        breed = BreedService.get_or_create(breed_name)
        new_pet = Pet(name=name, user_id=user_id, breed_id=breed.id)
        db.session.add(new_pet)
        return new_pet
    
    def get_pets_by_user(idx=None):
        if idx:
            pets = Pet.query.filter_by(user_id = idx).all()
        else:
            pets = Pet.query.all()
        return pets

class BreedService:
    @staticmethod
    @commit_after
    def create_breed(breed):
        new_breed = Breed(breed=breed)
        db.session.add(new_breed)
        return new_breed
         

    @staticmethod
    def get_or_create(breed):
        result = Breed.query.filter_by(breed=breed).first()
        if result is None:
            result = BreedService.create_breed(breed)
        return result
