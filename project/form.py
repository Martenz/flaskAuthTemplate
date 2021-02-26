from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DecimalField
from wtforms.validators import DataRequired
from wtforms import Form, BooleanField, StringField, PasswordField, validators

class AddPoint(Form):
    name = StringField('Title', [validators.Length(min=4, max=50)], render_kw={'class':'form-control','style':''})
    latitude = DecimalField('Latitude', render_kw={'class':'form-control','style':''})
    longitude = DecimalField('Longitude', render_kw={'class':'form-control','style':''})
    #coordinates = StringField('Coordinates', [validators.Length(min=0, max=250)], render_kw={'class':'form-control','style':''})
    body = TextAreaField('Description', [validators.Length(min=0, max=5000)])