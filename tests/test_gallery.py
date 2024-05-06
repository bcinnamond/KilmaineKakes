# Tests for gallery page and routes

def test_gallery(app, client):
    res = client.get('/gallery')


    gallery_data = res.get_json()

    assert isinstance(gallery_data, list)
    assert len(gallery_data) > 1