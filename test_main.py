from main import app


def test_home():
    client = app.test_client()
    response = client.get('/')

    assert response.status_code == 200
    assert response.data == b"Welcome to the CloudOps Application!"


def test_health():
    client = app.test_client()
    response = client.get('/health')

    assert response.status_code == 200
    assert response.json == {"status": "UP"}
