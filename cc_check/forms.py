from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired

from wtforms import SubmitField


class CCCForm(FlaskForm):
    numbers = FileField("Upload your credit card numbers", validators=[FileRequired()])
    submit = SubmitField('Submit')
