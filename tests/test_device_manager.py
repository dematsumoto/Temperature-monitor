def test_login_required(client):
    response = client.get('/devices')
    assert response.headers['Location'] == 'http://localhost/auth/login'


def test_device_list(client, auth):
    auth.login()
    response = client.get('/devices')
    assert b'test sensor 1' in response.data
    assert b'test sensor 2' in response.data
    assert b'test sensor 3' not in response.data


def test_add_device(client, auth):
    auth.login()
    response_init = client.get('/devices')
    assert response_init.status_code == 200
    assert b'test device 1' not in response_init.data

    client.post('/add_device', data={'device_id': '999', 'description': 'test device 1'})

    response = client.get('/devices')
    assert response.status_code == 200
    assert b'test device 1' in response.data


def test_add_device_without_id(client, auth):
    auth.login()
    response = client.post('/add_device', data={'device_id': '', 'description': 'test device'})
    assert b'Device ID is required.' in response.data


def test_add_device_without_description(client, auth):
    auth.login()
    response = client.post('/add_device', data={'device_id': '1000', 'description': ''})
    assert b'Description is required.' in response.data


def test_delete_device(client, auth):
    auth.login()
    client.post('/add_device', data={'device_id': '999', 'description': 'test device 1'})
    assert b'test device 1' in client.get('/devices').data

    response = client.post('/999/delete')
    assert b'test device 1' not in response.data


def test_delete_device_without_ownership(client, auth):
    auth.login()

    response = client.post('/3/delete')
    assert response.status_code == 403
    assert b'Permission denied.' in response.data


def test_delete_nonexistent_device(client, auth):
    auth.login()
    response = client.post('/9000/delete')
    assert response.status_code == 404
    assert b'Device id 9000 doesn\'t exist.' in response.data


def test_delete_login_required(client):
    response = client.post('/999/delete')
    assert response.headers['Location'] == 'http://localhost/auth/login'


