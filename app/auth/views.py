from . import auth
from flask import render_template, flash, redirect, url_for, session, request
from datetime import datetime
from .forms import LoginForm
from flask_login import login_user, logout_user
from ..models import User


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            flash('login success')
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password')
    return render_template('auth/index.html', current_time=datetime.utcnow(), form=form)


@auth.route('/logout')
def logout():
    logout_user()
    flash('you have already logged out')
    return redirect(url_for('main.index'))

