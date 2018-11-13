from . import main
from flask import render_template, flash, redirect, url_for, session
from datetime import datetime
from flask_login import login_required


@main.route('/')
def index():
    return render_template('main/index.html', current_time=datetime.utcnow())


@main.route('/admin123')
@login_required
def admin():
    return render_template('main/admin.html', current_time=datetime.utcnow())



