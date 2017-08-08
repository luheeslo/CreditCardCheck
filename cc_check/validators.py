from wtforms.validators import ValidationError

from cc_check.core import validate_cc_number

class CreditCardNumber:
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        if not validate_cc_number(field.data or ''):
            if self.message is None:
                self.message = 'Invalid'
            raise ValidationError(self.message)
