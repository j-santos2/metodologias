from urllib import request
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required

from ..services import PetService

class Petxd:
    def __init__(self, idx, name, breed):
        self.id = idx
        self.name = name
        self.breed = breed

pet = Blueprint('pet', __name__,
                        template_folder='templates')

@pet.route('/', methods=['GET', 'POST'])
# @login_required
def pet_main():
    if request.method == 'POST':
        data = []
        data.append(request.form.get('name'))
        data.append(current_user.id)
        data.append(request.form.get('breed'))
        new_pet = PetService.create_user(data[0], data[1], data[2])
        if new_pet is None:
            return render_template(f'pet/pets.html', error_message='Something went wrong. Please try again')    
        return redirect(url_for('pet.pet_main'))
    elif request.method == 'GET':
        my_pets = [
            Petxd(1, 'juan', 'bullterrier'),
            Petxd(1, 'juan', 'boxer'),
        ]
        return render_template(f'pet/pets.html', pets=my_pets)

@pet.route('/<int:_id>', methods=['GET'])
# @login_required
def pet_o(_id):
    pet_data = Petxd(_id, 'juan', 'bullterrier')
    return render_template(f'pet/pet.html', pet=pet_data)
