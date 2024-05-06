# Tests for contact page and routes

def test_contact(app, client):
    res = client.get('/contact')

    contact_data = res.get_json()

    assert isinstance(contact_data, list)
    assert len(contact_data) > 1