from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    DateField,
    SelectField,
    SelectMultipleField
)
from wtforms.validators import DataRequired

from . import FESTIVAL_START, FESTIVAL_END
from .validators import Before, After


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('remember me')
    submit = SubmitField('Sign In')


class ReservationForm(FlaskForm):
    during_festival = [After(FESTIVAL_START,
                             message=f'The festival starts the {FESTIVAL_START}'),
                       Before(FESTIVAL_END,
                              message=f'The festival end the {FESTIVAL_END}')]
    vips = SelectMultipleField('VIPs', validators=[DataRequired()])
    date_arrival = DateField('Day arrival', validators=during_festival)
    departure_validator = [After(date_arrival,
                                 message='Departure date must be after arrival date')] \
                           + during_festival 
    date_departure = DateField('Day departure',
                               validators=departure_validator)
    submit = SubmitField('Proceed')
