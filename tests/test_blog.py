# Tests for blog page and routes

def test_blog(app, client):
    res = client.get('/blog')
    assert res.status_code == 200