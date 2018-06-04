def test_login(client):
    response = client.get('/')
    assert response.status_code == 200
