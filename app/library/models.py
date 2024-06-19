from app.extensions import db
from sqlalchemy import Integer, String, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from app.user.models import User


class Book(db.Model):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]
    year: Mapped[int] = mapped_column(SmallInteger)
    reviews = db.relationship('Review', backref='book', lazy='dynamic')

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class Review(db.Model):
    __tablename__ = 'reviews'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, db.ForeignKey('users.id'))
    book_id: Mapped[int] = mapped_column(Integer, db.ForeignKey('books.id'))
    review: Mapped[str]

    def __str__(self):
        return self.review
