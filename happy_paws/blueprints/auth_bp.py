from urllib import request
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, logout_user


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
            return render_template(f'auth/register.html', loggeado=current_user.is_authenticated, error_message='User is already register. Have you forgotten your password?')    
        return redirect(url_for('auth.login', loggeado=current_user.is_authenticated))
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
            return redirect(url_for('index.show', loggeado=current_user.is_authenticated))
        return render_template(f'auth/login.html', loggeado=current_user.is_authenticated, error_message='Nombre de usuario y/o contraseña incorrectos')

    elif request.method == 'GET':
        return render_template(f'auth/login.html', loggeado=current_user.is_authenticated)

@auth.route('/logout', methods=['GET'])
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect(url_for('index.show', loggeado=current_user.is_authenticated))
