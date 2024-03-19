from myapp import db, app
from flask import render_template, redirect, url_for, request, flash, abort
from flask_login import login_user, login_required, logout_user
from myapp.models import User
from mapp.forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/wecome')
@login_required
def welcome_user():
    return render_template('welcome.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('home'))

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
    
    if user.check_password(form.password.data) and user is not none:
        login_user(user)
        flash("Logged in successfully!")
        # login?next=dashboard
        next = request.args.get('next')

        if next == None or not next[0] == '/':
            next = url_for('welcome_user')

        return redirect(next)


# @app.route('/register')