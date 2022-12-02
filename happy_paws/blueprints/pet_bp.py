from urllib import request
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required

from ..services import PetService, UserService


pet = Blueprint('pet', __name__, template_folder='templates')

@pet.route('/pet/add', methods=['GET', 'POST'])
@login_required
def pet_add():
    if request.method == 'POST':
        data = []
        data.append(request.form.get('name'))
        data.append(current_user.id)
        data.append(request.form.get('breed'))
        new_pet = PetService.create_pet(data[0], data[1], data[2])
        if new_pet is None:
            my_pets = PetService.get_pets_by_user(idx=current_user.id)
        return redirect(url_for('pet.pet_main'))
    elif request.method == 'GET':
        my_pets = PetService.get_pets_by_user(idx=current_user.id)
        return render_template(f'pet/add_pet.html', loggeado=current_user.is_authenticated, pets=my_pets)

@pet.route('/pet', methods=['GET'])
@login_required
def pet_main():
    my_pets = UserService.get_user_pets(current_user.id)
    return render_template(f'pet/pets.html', loggeado=current_user.is_authenticated, pets=my_pets)
