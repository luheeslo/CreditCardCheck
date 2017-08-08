import pytest

from cc_check import app as main_app


@pytest.fixture
def app():
    main_app.debug = True
    return main_app
