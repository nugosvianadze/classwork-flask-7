from app.extensions import db
from sqlalchemy import Integer, String, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from app.user.models import User


class Book(db.Model):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str]
    author: Mapped[str]
    year: Mapped[int] = mapped_column(SmallInteger)
    reviews = db.relationship('Review', backref='book', lazy='dynamic')

    def __repr__(self):
        return '<Book %r>' % self.title

    def __str__(self):
        return self.title


class Review(db.Model):
    __tablename__ = 'reviews'
    id = mapped_column(Integer, primary_key=True)
    book_id = mapped_column(Integer, db.ForeignKey('books.id'))
    user_id = mapped_column(Integer, db.ForeignKey('users.id'))
    rating = mapped_column(SmallInteger)
    review = mapped_column(String(500))

    def __repr__(self):
        return '<Review %r>' % self.id

    def __str__(self):
        return self.id