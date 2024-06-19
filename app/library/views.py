import os

from flask import Blueprint, render_template, request, session, redirect, url_for, flash

from .forms import ReviewCreateForm
from .models import Book, Review
from app.user.models import User
from app.extensions import db

from flask_login import current_user

template_folder = os.path.abspath('app/templates')
library_bp = Blueprint('library', __name__,
                       template_folder=template_folder)


@library_bp.route('/')
def home():
    return render_template('library/home.html')


@library_bp.route('/book-list')
def book_list():
    books = db.session.query(Book).all()
    return render_template('library/book-list.html', books=books)


@library_bp.route('/book-review/<int:book_id>', methods=['GET', 'POST'])
def book_review(book_id: int):
    form = ReviewCreateForm()
    book = db.session.get(Book, book_id)
    if request.method == 'POST':
        if form.validate_on_submit():
            review = form.review.data
            review_obj = Review(user=current_user, book=book, review=review)
            db.session.add(review_obj)
            db.session.commit()
            flash('Review Successfully Created!')
            return render_template('library/book-review.html', book=book, form=form)
        return render_template('library/book-review.html', book=book, form=form)
    return render_template('library/book-review.html', book=book, form=form)


@library_bp.route('/delete-review/<int:review_id>')
def delete_review(review_id: int):
    review = db.session.get(Review, review_id)
    db.session.delete(review)
    db.session.commit()
    flash('Review Successfully Deleted!!')
    return redirect(url_for('user.home'))
