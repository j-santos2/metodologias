from urllib import request
from flask import Blueprint, render_template, request, redirect, url_for

from ..services import UserService


auth = Blueprint('auth', __name__,
                        template_folder='templates')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = []
        data.append(request.form.get('email'))
        data.append(request.form.get('username'))
        data.append(request.form.get('password'))
        new_user = UserService.create_user(data[0], data[1], data[2])
        if new_user is None:
            return render_template(f'auth/register.html', error_message='User is already register. Have you forgotten your password?')    
        return redirect(url_for('auth.login'))
    elif request.method == 'GET':
        return render_template(f'auth/register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = []
        data.append(request.form.get('username'))
        data.append(request.form.get('password'))
        ret_val = UserService.authenticate(data[0], data[1])
        if ret_val:
            return render_template(f'auth/login.html', message='Logged in successfully')
        return render_template(f'auth/login.html', error_message='Wrong username and/or password. Try again')

    elif request.method == 'GET':
        return render_template(f'auth/login.html')
