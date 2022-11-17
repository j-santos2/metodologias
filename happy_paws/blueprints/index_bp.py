from flask import Blueprint, render_template
from flask_login import current_user

index = Blueprint('index', __name__,
                        template_folder='templates')

@index.route('/')
def show():
    return render_template(f'index/index.html', loggeado=current_user.is_authenticated)
