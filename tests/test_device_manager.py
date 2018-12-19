import pytest
from flaskr.db import get_db


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

    client.post('/add_device', data={'description': 'test device 1'})

    response = client.get('/devices')
    assert response.status_code == 200
    assert b'test device 1' in response.data


def test_add_device_without_description(client, auth):
    auth.login()
    response = client.post('/add_device', data={'description': ''})
    assert b'Description is required.' in response.data

