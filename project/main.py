from flask import Blueprint, render_template, request, flash, redirect, url_for
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
    points = Points.query.all()
    if current_user.is_authenticated:

        if request.method == 'POST' and form.validate():
            point = Points(name=form.name.data, latitude=str(form.latitude.data), longitude=str(form.longitude.data), body=form.body.data)
            db.session.add(point)
            db.session.commit()
            flash("Point Page Added", "success")
            return redirect(url_for('main.mainmap'))
        else:
            return render_template('map.html', name=current_user.name, form=form, points = points)
    else:
        return render_template('map.html', points = points)

@main.route('/map/<id>')
def pointmap(id=None):
    point = Points.query.filter_by(id = id).one()
    if not id:
        return redirect(url_for('main.mainmap'))
    return render_template('point_map.html', point = point)