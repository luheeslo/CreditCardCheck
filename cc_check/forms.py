from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

from cc_check.validators import CreditCardNumber


class CCCForm(FlaskForm):
    number = StringField("What is your credit card number?", validators=[Required(), CreditCardNumber()])
    submit = SubmitField('Submit')
