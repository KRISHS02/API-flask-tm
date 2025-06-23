import pytest
from app import app as flask_app

@pytest.fixture(scope='module')
def app():
    flask_app.config['TESTING'] = True
    return flask_app

@pytest.fixture
def client(app):
    return app.test_client()
