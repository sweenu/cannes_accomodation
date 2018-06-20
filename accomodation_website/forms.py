from flask_wtf import FlaskForm
from wtforms import (
    DateField,
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
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
    start = FESTIVAL_START.strftime('%d/%m/%Y')
    end = FESTIVAL_END.strftime('%d/%m/%Y')
    during_festival = [After(FESTIVAL_START, message=f'The festival starts the {start}'),
                       Before(FESTIVAL_END, message=f'The festival ends the {end}')]
    departure_validator = [After('date_arrival',
                                 message='Departure date must be after arrival date')] \
                           + during_festival 
    datefield_defaults = {'format': '%d/%m/%Y'}

    vips = SelectMultipleField('VIPs', coerce=int, validators=[DataRequired()])
    date_arrival = DateField('Day arrival', **datefield_defaults,
                             validators=during_festival)
    date_departure = DateField('Day departure', **datefield_defaults,
                               validators=departure_validator)
    submit = SubmitField('Proceed')
