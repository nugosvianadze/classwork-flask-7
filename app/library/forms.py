from wtforms import TextAreaField, SubmitField
from flask_wtf import FlaskForm


class ReviewCreateForm(FlaskForm):
    review = TextAreaField('Review')
    submit = SubmitField('Submit')
