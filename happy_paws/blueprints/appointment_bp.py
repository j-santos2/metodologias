from urllib import request
import datetime

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required

from ..services import AppointmentService, PetService, UserService

class Appoinmentxd:
    def __init__(self, idx, name, breed):
        self.id = idx
        self.name = name
        self.breed = breed

appointment = Blueprint('appointment', __name__, template_folder='templates')

@appointment.route('/appointment/add', methods=['GET', 'POST'])
@login_required
def appointment_add():
    if request.method == 'POST':
        data = []
        pet_id = int(request.form.get('pet_id'))
        data.append(pet_id)
        data.append(current_user.id)
        schedule = datetime.datetime.strptime(request.form.get('schedule'), '%Y-%m-%dT%H:%M')
        data.append(schedule)
        print(data)
        new_appointment = AppointmentService.create_appointment(data[0], data[1], data[2])
        if new_appointment is None:
            return render_template(f'appointment/add_appointment.html', loggeado=current_user.is_authenticated, error_message='Something went wrong. Please try again')    
        return redirect(url_for('appointment.appointment_main', loggeado=current_user.is_authenticated))
    elif request.method == 'GET':
        pets = PetService.get_pets_by_user(current_user.id)
        return render_template(f'appointment/add_appointment.html', loggeado=current_user.is_authenticated, pets=pets)

@appointment.route('/appointment', methods=['GET'])
@login_required
def appointment_main():
    pets = UserService.get_user_pets(current_user.id)
    return render_template(f'appointment/appointments.html', loggeado=current_user.is_authenticated, pets=pets)
