# Tests for login page and routes

def test_login(app, client):
    res = client.get('/login')
    assert res.status_code == 200

def test_owner_login(app, client):
    res = client.post('/owner_login', data={'username': 'kilmainekakes', 'password': 'K1lma1n3KaK3s!'})
    assert res.status_code == 302  # Assuming you're redirecting upon successful login