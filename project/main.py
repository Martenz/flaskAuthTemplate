from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/map')
# @login_required
def mainmap():
    if current_user.is_authenticated:
        return render_template('map.html', name=current_user.name)
    else:
        return render_template('map.html')
