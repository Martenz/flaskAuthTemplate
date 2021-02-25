from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db
from .form import AddPoint
from .models import Points

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/map', methods=['GET', 'POST'])
# @login_required
def mainmap():
    form = AddPoint(request.form)
    if current_user.is_authenticated:

        if request.method == 'POST' and form.validate():
            point = Points(name=form.name.data, coordinates=form.coordinates.data)
            db.session.add(point)
            db.session.commit()
            return render_template('map.html', name=current_user.name + " Point added.", form=form)
        else:
            return render_template('map.html', name=current_user.name, form=form)
    else:
        return render_template('map.html')
