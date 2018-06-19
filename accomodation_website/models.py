from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from . import db, login_manager


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, index=True, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    staff = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Accomodation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    total_rooms = db.Column(db.Integer)
    available_rooms = db.relationship('AvailableRooms')
    type = db.Column(db.String(64))

    services = db.relationship('Service', secondary='accomodation_service',
                               backref=db.backref('accomodations', lazy='dynamic'))

    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    owner = db.relationship('User', backref='accomodations')

    def __repr__(self):
        return f'<Accomodation {self.name}>'


class AvailableRooms(db.Model):
    number = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, primary_key=True, nullable=False)
    accomodation_id = db.Column(db.Integer, db.ForeignKey('accomodation.id'))


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return f'<Service {self.name}>'


class AccomodationService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    accomodation_id = db.Column(db.Integer,
                                db.ForeignKey('accomodation.id', ondelete='CASCADE'))
    service_id = db.Column(db.Integer,
                           db.ForeignKey('service.id', ondelete='CASCADE'))


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    vip_id = db.Column(db.Integer, db.ForeignKey('VIP.id'))
    vip = db.relationship('VIP', backref='reservations')

    accomodation_id = db.Column(db.Integer, db.ForeignKey('accomodation.id'))
    accomodation = db.relationship('Accomodation', backref='reservations', uselist=False)

    date_arrival = db.Column(db.Date, nullable=False)
    date_departure = db.Column(db.Date, nullable=False)
    
    def get_stay_length(self):
        return self.date_departure - self.date_arrival
        

class VIP(db.Model):
    __tablename__ = 'VIP'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    

class Juror(VIP):
    pass


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
