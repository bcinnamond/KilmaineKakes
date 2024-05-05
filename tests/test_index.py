# Tests for index page and routes

def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
