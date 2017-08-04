import pytest

from cc_check.core import validate_cc_number


@pytest.mark.parametrize('testcase', [
    # Valid Credit Card Numbers
    ('4253625879615786', True),
    ('4424424424442444', True),
    ('5122-2368-7954-3214', True),
    #  Invalid Credit Card Numbers
    ('42536258796157867', False),
    ('4424444424442444', False),
    ('5122-2368-7954 - 3214', False),
    ('44244x4424442444', False),
    ('0525362587961578', False),

])
def test_validate_cc_number(testcase):
    assert validate_cc_number(testcase[0]) == testcase[1]
