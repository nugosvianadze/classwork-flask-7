from bcrypt import hashpw, gensalt, checkpw
from flask_login import UserMixin

from app.extensions import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class User(db.Model):
    __tablename__ = 'users'
    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(String(80))
    email = mapped_column(String(120), unique=True, nullable=False)
    password = mapped_column(String(120), nullable=False)
    reviews = db.relationship('Review', backref='user', lazy='dynamic')

    @staticmethod
    def set_password(password):
        return hashpw(password.encode('utf-8'), gensalt())

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.set_password(password)

    def __repr__(self):
        return '<User %r>' % self.username

    def __str__(self):
        return self.username

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return self.is_active

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return str(self.id)
        except AttributeError:
            raise NotImplementedError("No `id` attribute - override `get_id`") from None

    @classmethod
    def check_credentials(cls, email, password):
        user = User.query.filter_by(email=email).first()
        if not user or not checkpw(password.encode('utf-8'), user.password):
            return None
        return user
