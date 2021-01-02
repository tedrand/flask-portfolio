import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

import os
from dotenv import load_dotenv

load_dotenv()

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form['username'])
        print(request.form['password'])
        print(os.getenv('APP_USER'))
        print(os.getenv('APP_PASSWORD'))
        username = request.form['username']
        password = request.form['password']

        if username == os.getenv('APP_USER') and password == os.getenv('APP_PASSWORD'):
            session.clear()
            session['user_id'] = os.getenv('USER_ID')
            return redirect(url_for('index'))

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = {
            'username': os.getenv('APP_USER'),
            'password': os.getenv('APP_PASSWORD')
        }

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view