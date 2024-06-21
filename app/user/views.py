import os
from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, logout_user, login_required, current_user
from bcrypt import hashpw, checkpw, gensalt

from .models import User
from app.extensions import db, login_manager
from .forms import LoginForm, RegisterForm

template_folder = os.path.abspath('app/templates')
user_bp = Blueprint('user', __name__, url_prefix='/user', template_folder=template_folder)


@login_manager.user_loader
def load_user(user):
    return db.session.get(User, user)


@user_bp.route('/')
@login_required
def home():
    return render_template('user/user-profile.html')


@user_bp.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            user = User.query.filter_by(email=email).first()
            if not user or not checkpw(password.encode('utf-8'), user.password):
                flash('Invalid Credentials! Try Again')
                return render_template('user/login.html', form=form)
            print(user)
            # session['email'] = user.email
            # session['user_id'] = user.id
            login_user(user)
            return redirect(url_for('user.home'))
        return render_template('user/login.html', form=form)
    return render_template('user/login.html', form=form)


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            user = User.query.filter_by(email=email).first()
            if user:
                flash('User With This Email Already Exist')
                return render_template('user/registration.html', form=form)
            hashed_password = hashpw(password.encode('utf-8'), gensalt())

            new_user = User(username=username,
                            email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('user.login'))
        return render_template('user/registration.html', form=form)
    return render_template('user/registration.html', form=form)


@user_bp.route('/logout')
@login_required
def logout():
    # session.pop('user_id', None)
    # session.pop('email', None)
    logout_user()
    flash('Successfully Logged Out')
    return redirect(url_for('user.login'))
