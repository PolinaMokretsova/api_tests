import allure
from pytest_voluptuous import S
from schemas.reqres import single_user, register, create, update
from utils.helpers import authorization, data_register, data_create, data_update
from utils.sessions import reqres


def test_single_user():
    response = reqres().get('/api/users/2', cookies=authorization())

    with allure.step('status code is 200'):
        assert response.status_code == 200
    with allure.step('single_user schema is correct'):
        assert S(single_user) == response.json()


def test_register():
    response = reqres().post('/api/register', cookies=authorization(), data=data_register())

    with allure.step('status code is 200'):
        assert response.status_code == 200
    with allure.step('"id" in response = 4'):
        assert int(response.json()['id']) == 4
    with allure.step('register schema is correct'):
        assert S(register) == response.json()


def test_create():
    response = reqres().post('/api/users', cookies=authorization(), data=data_create())

    with allure.step('status code is 201'):
        assert response.status_code == 201
    with allure.step('"name" in response = morpheus'):
        assert str(response.json()['name']) == 'morpheus'
    with allure.step('"job" in response = leader'):
        assert str(response.json()['job']) == 'leader'
    with allure.step('create schema is correct'):
        assert S(create) == response.json()


def test_update():
    response = reqres().put('/api/users/2', cookies=authorization(), data=data_update())

    with allure.step('status code is 200'):
        assert response.status_code == 200
    with allure.step('"name" in response = morpheus'):
        assert str(response.json()['name']) == 'morpheus'
    with allure.step('"job" in response = zion resident'):
        assert str(response.json()['job']) == 'zion resident'
    with allure.step('update schema is correct'):
        assert S(update) == response.json()


def test_delayed_response():
    response = reqres().get('/api/users?delay=3', cookies=authorization())

    with allure.step('status code is 200'):
        assert response.status_code == 200
