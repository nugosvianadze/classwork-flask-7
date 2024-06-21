from wtforms import TextAreaField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import data_required


class ReviewCreateForm(FlaskForm):
    review = TextAreaField('Review', validators=[data_required()])
    submit = SubmitField('Submit')
