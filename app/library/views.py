import os

from flask import Blueprint, render_template

template_folder = os.path.abspath('app/templates')
library_bp = Blueprint('library', __name__,
                       template_folder=template_folder)


@library_bp.route('/')
def home():
    return render_template('library/home.html')


@library_bp.route('/book-list')
def book_list():
    return render_template('library/book-list.html')


@library_bp.route('/book-review')
def book_review():
    return render_template('library/book-review.html')
