import click
from flask.cli import AppGroup

from happy_paws import create_app, create_database
from happy_paws.services import UserService, PetService, BreedService, AppointmentService

app = create_app()

@app.cli.command('init', help='Creates and initializes database')
def initialize():
    create_database(app)
    print('Database initialized')

user_cli = AppGroup('user', help='User object commands')

@user_cli.command('create', help='Creates a user')
@click.argument('email')
@click.argument('name')
@click.argument('password')
@click.argument('role', type=click.INT)
def create_user(email, name, password, role):
    ret_val = UserService.create_user(email, name, password, role)
    print(f'New user: {ret_val}')

app.cli.add_command(user_cli)

pet_cli = AppGroup('pet', help='Pet object commands')

@pet_cli.command('create', help='Creates a Pet')
@click.argument('name')
@click.argument('user_id', type=click.INT)
@click.argument('breed')
def create_pet(name, user_id, breed):
    ret_val = PetService.create_pet(name, user_id, breed)
    print(f'New Pet: {ret_val}')

app.cli.add_command(pet_cli)

breed_cli = AppGroup('breed', help='Breed object commands')

@breed_cli.command('create', help='Creates a Breed')
@click.argument('breed')
def create_breed(breed):
    ret_val = BreedService.create_breed(breed)
    print(f'New Breed: {ret_val}')

app.cli.add_command(breed_cli)

appointment_cli = AppGroup('appointment', help='Appointment object commands')

@appointment_cli.command('create', help='Creates a Appointment')
@click.argument('pet_id')
@click.argument('user_id')
@click.argument('schedule', type=click.DateTime(formats=['%Y-%m-%dT%H:%M:%S']))
def create_appointment(pet_id, user_id, schedule):
    ret_val = AppointmentService.create_appointment(pet_id, user_id, schedule)
    print(f'New Appointment: {ret_val}')

@appointment_cli.command('get', help='Gets all Appointment')
@click.argument('user_id')
def create_appointment(user_id):
    ret_val = AppointmentService.get_appointments(user_id)
    print(f'Appointments:\n{ret_val}')

app.cli.add_command(appointment_cli)
