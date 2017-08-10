from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed

from wtforms import SubmitField


class CCCForm(FlaskForm):
    numbers = FileField("Upload your credit card numbers:", validators=[
        FileRequired(),
        FileAllowed(['txt'], '.txt format only!')])
    submit = SubmitField('Submit')
