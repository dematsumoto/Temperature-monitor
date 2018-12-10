import pytest
from flaskr.db import get_db


def test_login_required(client):
    response = client.get('/')
    assert response.headers['Location'] == 'http://localhost/auth/login'


def test_index(client, auth):
    auth.login()
    response = client.get('/')
    assert b'Log Out' in response.data
    assert b'test sensor' in response.data
    assert b'33' in response.data
    assert b'2018-01-01 00:00:00' in response.data

