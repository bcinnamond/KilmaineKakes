# Tests for gallery page and routes

def test_gallery(app, client):
    res = client.get('/gallery')
    assert res.status_code == 200