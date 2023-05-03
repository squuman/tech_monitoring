import json
import pytest
import allure

from data import generate_products


@allure.story("Создание продукта")
@pytest.mark.parametrize('data', generate_products())
def test_create_product(api, data):
    with allure.step("Отправка запроса для создания продукта"):
        create_product = api.create_product(data)
        assert 201 == create_product.status_code
    with allure.step("Получение продукта"):
        response = json.loads(api.get_products(search=data['title']).text)

        assert 1 == response['results']
        assert data['title'] == response['products'][0]['title']

        # Чистка бд
        api.delete_product(str(response['products'][0]['id']))


@allure.story("Получения списка продуктов")
def test_get_products(api, create_product):
    with allure.step("Отправка запроса для получения списка продуктов"):
        response = api.get_products()

        products = json.loads(response.text)['products']

        assert isinstance(products, list)


@allure.story("Изменение продукта")
def test_update_product(api, create_product):
    with allure.step("Отправка запроса для изменение продукта"):
        new_title = 'updated title'
        api.update_product(str(create_product['id']), {
            "title": new_title,
        })
    with allure.step("Получение продукта"):
        response = api.get_product(str(create_product['id']))
        product = json.loads(response.text)

        assert new_title == product['title']


@allure.story("Удаление продукта")
def test_delete_product(api, create_product):
    with allure.step("Отправка запроса на удаление продукта"):
        api.delete_product(str(create_product['id']))
    with allure.step("Отправка запроса для получения продукта"):
        response = api.get_product(str(create_product['id']))
        message = json.loads(response.text)['detail']

        assert f"No note with this id: {create_product['id']} found" == message
