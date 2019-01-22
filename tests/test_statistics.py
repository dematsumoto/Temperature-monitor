def test_login_required(client):
    response = client.get('/stats')
    assert response.headers['Location'] == 'http://localhost/auth/login'


def test_get_data(client, auth):
    auth.login()
    response = client.get('/')
    assert b'test sensor 1' in response.data
    assert b'11.1' in response.data
    assert b'2018-01-01 00:00:00' in response.data

    assert b'test sensor 2' in response.data
    assert b'22.2' in response.data
    assert b'2018-02-02 00:00:00' in response.data

    assert b'test sensor 3' not in response.data
    assert b'33.3' not in response.data
    assert b'2018-03-03 00:00:00' not in response.data

