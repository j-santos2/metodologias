from urllib import request
from flask import Blueprint, render_template, request, redirect, url_for

auth = Blueprint('auth', __name__,
                        template_folder='templates')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    return render_template(f'auth/register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template(f'auth/login.html')
