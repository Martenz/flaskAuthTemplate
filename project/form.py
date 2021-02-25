from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms import Form, BooleanField, StringField, PasswordField, validators

class AddPoint(Form):
    name = StringField('Title', [validators.Length(min=4, max=50)])
    coordinates = StringField('Coordinates', [validators.Length(min=0, max=250)])