import requests
from pytest_voluptuous import S
from schemas.reqres import single_user, register, create, update


def test_single_user():
    response = requests.get("https://reqres.in/api/users/2")

    assert response.status_code == 200
    assert S(single_user) == response.json()


def test_register():
    response = requests.post("https://reqres.in/api/register", data={
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    })

    assert response.status_code == 200
    assert int(response.json()['id']) == 4
    assert S(register) == response.json()


def test_create():
    response = requests.post("https://reqres.in/api/users", data={
        "name": "morpheus",
        "job": "leader"
    })

    assert response.status_code == 201
    assert str(response.json()['name']) == 'morpheus'
    assert str(response.json()['job']) == 'leader'
    assert S(create) == response.json()


def test_update():
    response = requests.put("https://reqres.in/api/users/2", data={
        "name": "morpheus",
        "job": "zion resident"
    })

    assert response.status_code == 200
    assert str(response.json()['name']) == 'morpheus'
    assert str(response.json()['job']) == 'zion resident'
    assert S(update) == response.json()


def test_delete():
    response = requests.delete("https://reqres.in/api/users/2")

    assert response.status_code == 204
