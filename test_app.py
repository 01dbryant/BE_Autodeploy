import pytest
from flask_app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'API is running' in response.data

def test_health(client):
    """Test the health endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    assert b'healthy' in response.data

def test_status(client):
    """Test the status endpoint"""
    response = client.get('/status')
    assert response.status_code == 200
    assert b'CI/CD pipeline working' in response.data
