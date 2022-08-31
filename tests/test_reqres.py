import allure
import requests
from pytest_voluptuous import S
from schemas.reqres import single_user, register, create, update
from utils.sessions import reqres


def test_single_user():
    response = reqres().get('/api/users/2')

    assert response.status_code == 200
    assert S(single_user) == response.json()


def test_register():
    response = reqres().post('/api/register', data={
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    })

    assert response.status_code == 200
    assert int(response.json()['id']) == 4
    assert S(register) == response.json()


def test_create():
    response = reqres().post('/api/users', data={
        "name": "morpheus",
        "job": "leader"
    })

    assert response.status_code == 201
    assert str(response.json()['name']) == 'morpheus'
    assert str(response.json()['job']) == 'leader'
    assert S(create) == response.json()


def test_update():
    response = reqres().put('/api/users/2', data={
        "name": "morpheus",
        "job": "zion resident"
    })

    assert response.status_code == 200
    assert str(response.json()['name']) == 'morpheus'
    assert str(response.json()['job']) == 'zion resident'
    assert S(update) == response.json()


def test_delayed_response():
    response = reqres().get('/api/users?delay=3')

    assert response.status_code == 200
