import pytest

from cc_check import app as main_app


@pytest.fixture
def app():
    main_app.config['DEBUG'] = True
    main_app.config['WTF_CSRF_ENABLED'] = False
    return main_app
