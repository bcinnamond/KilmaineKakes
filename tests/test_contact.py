# Tests for contact page and routes

def test_contact(app, client):
    res = client.get('/contact')
    assert res.status_code == 200