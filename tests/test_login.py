# Tests for login page and routes

def test_login(app, client):
    res = client.get('/login')
    assert res.status_code == 200
