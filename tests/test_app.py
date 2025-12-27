"""Unit tests for the Flask application."""

import pytest
from app import app as flask_app


@pytest.fixture(scope='module')
def client():
    """Create a test client for the Flask application."""
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as test_client:
        yield test_client


def test_health_check(client):
    """Test the /health endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}


def test_index(client):
    """Test the main / endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    assert 'message' in response.json
