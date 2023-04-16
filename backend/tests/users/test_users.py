import json
import pytest
import allure

from data import generate_users


@allure.story("Создание пользователя")
@pytest.mark.parametrize('data', generate_users())
def test_create_user(api, data):
    with allure.step("Отправка запроса для создания пользователя"):
        create_user = api.create_user(data)
        assert 201 == create_user.status_code
    with allure.step("Получение пользователя"):
        response = json.loads(api.get_users(search=data['name']).text)

        assert 1 == response['results']
        assert data['name'] == response['users'][0]['name']

        # Чистка бд
        api.delete_user(str(response['users'][0]['id']))


@allure.story("Получение списка пользователей")
def test_get_users(api, create_user):
    with allure.step("Отправка запроса для получения списка пользователей"):
        response = api.get_users()

        users = json.loads(response.text)['users']

        assert isinstance(users, list)


@allure.story("Изменение пользователя")
def test_update_user(api, create_user):
    with allure.step("Отправка запроса для изменение пользователя"):
        new_name = 'updated name'
        api.update_user(str(create_user['id']), {
            "login": create_user['login'],
            "password": create_user['password'],
            "name": new_name
        })
    with allure.step("Получение пользователя"):
        response = api.get_user(str(create_user['id']))
        user = json.loads(response.text)

        assert new_name == user['name']


@allure.story("Удаление пользователя")
def test_delete_user(api, create_user):
    with allure.step("Отправка запроса на удаление пользователя"):
        api.delete_user(str(create_user['id']))
    with allure.step("Отправка запроса для получения пользователя"):
        response = api.get_user(str(create_user['id']))
        message = json.loads(response.text)['detail']

        assert f"No note with this id: {create_user['id']} found" == message
