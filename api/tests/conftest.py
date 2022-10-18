# Create a test client using the Flask application configured for testing
import pytest
import config
from api.app import db
from api.routes import app
from api.models import Vehiculo,Inspeccion


@pytest.fixture
def client():
    app.config.from_object(config.TestingConfig)
    with app.test_client() as client: # app.test_client() is a function that returns a Flask application configured for testing
        with app.app_context(): # This is required to initialize the database
            yield client # yield is used to return the client to the test function

