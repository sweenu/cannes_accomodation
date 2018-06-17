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
    capacity = db.Column(db.Integer)
    type = db.Column(db.String(64))

    services = db.relationship('Service', secondary='accomodation_service',
                               backref=db.backref('accomodations', lazy='dynamic'))

    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    owner = db.relationship('User', backref='accomodations')

    def __repr__(self):
        return f'<Accomodation {self.name}>'


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return f'<Service {self.name}>'


class AccomodationService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    accomodation_id = db.Column(db.Integer(),
                                db.ForeignKey('accomodation.id', ondelete='CASCADE'))
    service_id = db.Column(db.Integer(),
                           db.ForeignKey('service.id', ondelete='CASCADE'))
    

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
