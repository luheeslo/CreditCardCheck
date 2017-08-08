import pytest

from cc_check.forms import CCCForm


@pytest.mark.parametrize('testcase', [
    # Valid Credit Card Numbers
    {'number': '5122-2368-7954-3214', 'expected': {}},
    #  Invalid Credit Card Numbers
    {'number': '0525362587961578', 'expected': {'number': ['Invalid']}},

])
def test_ccc_form(app, testcase):
    form = CCCForm()
    form.process(number=testcase['number'])
    form.validate()
    if 'csrf_token' in form.errors:
        del form.errors['csrf_token']
    assert form.errors == testcase['expected']
