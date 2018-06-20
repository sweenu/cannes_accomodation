import datetime

from accomodation_website import db, create_app
from accomodation_website.models import *


users = [
        User(username='gerard', staff=True, mail='gerard@cannes.com'),
        User(username='davdav', staff=True, mail='davdav@cannes.com'),
        User(username='juju', mail='juju@cannes.com'),
        User(username='matmat', mail='matmat@cannes.com'),
        User(username='plpl', mail='plpl@cannes.com'),
    ]
for i, user in enumerate(users):
    user.set_password(f'password{i}')


accomodations = [
        Accomodation(name="Le Palais de l'Intensité", owner=users[1], total_rooms=104),
        Accomodation(name="Le Patio Des Artistes", owner=users[2], total_rooms=87),
        Accomodation(name="Le Canberra", owner=users[3], total_rooms=5),
        Accomodation(name="Five Seas", owner=users[4], total_rooms=28),
    ]
for day in range(8, 19):
    date = datetime.date(2018, 5, day)
    for acco in accomodations:
        acco.available_rooms.append(AvailableRooms(number=acco.total_rooms,
                                                   date=date))
                                                   # accomodation_id=acco.id))


vips = [
        Juror(first_name='Lorem', last_name='Ipsum'),
        Juror(first_name='Paslorem', last_name='Pasipsum'),
        Juror(first_name='Pastroplorem', last_name='Pastropipsum'),
        Juror(first_name='Legerementlorem', last_name='Legermentipsum'),

        Guests(first_name='Henry', last_name='Fonda'),
        Guests(first_name='Brice', last_name='de Nice'),
        Guests(first_name='James', last_name='de Bond'),
        Guests(first_name='Tharace', last_name='Boulba'),
    ]


app = create_app()
with app.app_context():
    db.create_all()
    for obj in users + accomodations + vips:
        db.session.add(obj)
    db.session.commit()
