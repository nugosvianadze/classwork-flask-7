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

    def __repr__(self):
        return '<User %r>' % self.username

    def __str__(self):
        return self.username
