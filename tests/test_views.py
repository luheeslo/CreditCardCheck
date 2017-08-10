import re
from io import BytesIO

from flask import url_for


def test_main_post(client):
    test_txt = BytesIO(("6\n"
                "4123456789123456\n"
                "5123-4567-8912-3456\n"
                "61234-567-8912-3456\n"
                "4123356789123456\n"
                "5133-3367-8912-3456\n"
                "5123 - 3567 - 8912 - 3456").encode('utf-8'))
    expected = ['Valid', 'Valid', 'Invalid', 'Valid', 'Invalid', 'Invalid']

    response = client.post(url_for('main'),
                           content_type='multipart/form-data',
                           data={'numbers': (test_txt, 'test.txt')})

    match = re.findall(r'<td>(Valid|Invalid)</td>', response.get_data(as_text=True))

    assert match == expected
    assert response.status_code == 200
