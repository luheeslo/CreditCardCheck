import re


def validate_cc_number(number):
    if re.search(r'^[4-6](\d{3}\-\d{4}\-\d{4}\-\d{4}|\d{15})$', number):
        if not re.search(r'(\d)\1{3}', number):
            return True
    return False
