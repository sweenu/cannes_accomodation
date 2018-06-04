from flask import Blueprint, render_template, abort
from flask_login import current_user, logout_user, login_user, login_required

from .forms import LoginForm
from .models import User


bp = Blueprint('main', __name__)

@bp.route('/')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember.data)
        return redirect('/home')
    return render_template('login.html', form=form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@bp.route('/home')
@login_required
def home():
    accomodations = current_user.accomodations
    if len(accomodations) == 1:
        redirect(url_for('accomodation', id=accomodations[0].id))
    elif len(accomodations) > 1:
        render_template('accomodation_list.html', accomodations=accomodations)
    else:
        pass


@bp.route('/accomodations/<id>')
@login_required
def accomodation(id):
    accomodation = Accomodation.query.filter_by(id=id).first_or_404()
    if not accomodation.owner is current_user:
        abort(403)
    else:
        render_template('accomodation.html', accomodation=accomodation)
