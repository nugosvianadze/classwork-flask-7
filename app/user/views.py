import os
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user

from .models import User
from app.extensions import db, login_manager

template_folder = os.path.abspath('app/templates')
user_bp = Blueprint('user', __name__, url_prefix='/user', template_folder=template_folder)


@login_manager.user_loader
def load_user(user):
    return db.session.get(User, user)


@user_bp.route('/')
def home():
    return render_template('user/user-profile.html')


@user_bp.route('/login')
def login():
    return render_template('user/login.html')


@user_bp.route('/register')
def register():
    return render_template('user/registration.html')


@user_bp.route('/logout')
def logout():
    return redirect(url_for('user.login'))
