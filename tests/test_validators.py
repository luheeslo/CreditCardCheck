import pytest

from wtforms.validators import ValidationError

from cc_check.validators import CreditCardNumber

from tests.common import DummyField, DummyForm


@pytest.mark.parametrize('testcase', [
    # Valid Credit Card Numbers
    {'number': '4253625879615786', 'ok': True},
    {'number': '4424424424442444', 'ok': True},
    {'number': '5122-2368-7954-3214', 'ok': True},
    #  Invalid Credit Card Numbers
    {'number': '42536258796157867', 'ok': False},
    {'number': '4424444424442444', 'ok': False},
    {'number': '5122-2368-7954 - 3214', 'ok': False},
    {'number': '44244x4424442444', 'ok': False},
    {'number': '0525362587961578', 'ok': False},

])
def test_validate_credit_card_number(testcase):
    if testcase['ok']:
        assert CreditCardNumber()(DummyForm(), DummyField(data=testcase['number'])) == None
    else:
        with pytest.raises(ValidationError):
            CreditCardNumber()(DummyForm(), DummyField(data=testcase['number']))
