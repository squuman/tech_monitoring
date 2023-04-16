import json
import pytest
import allure


@allure.story("Получение продукта пользователя")
def test_get_users_product(api, create_users_product):
    with allure.step("Получение продукта пользователя"):
        products_response = api.get_users_product(search=create_users_product['user_id'])
        products = json.loads(products_response.text)

        assert 'users_products' in products
        assert isinstance(products['users_products'], list)


@allure.story("Создание продукта пользователя")
def test_create_users_product(api, create_users_product):
    with allure.step("Создание продукта пользователя"):
        products_response = api.get_users_product(search=create_users_product['user_id'])
        product = json.loads(products_response.text)['users_products'][0]

        assert create_users_product['user_id'] == product['user_id']
        assert create_users_product['product_id'] == product['product_id']


@allure.story("Удаление продукта пользователя")
def test_delete_users_product(api, create_users_product):
    with allure.step("Удаление продукта пользователя"):
        api.delete_users_product(str(create_users_product['id']))

        products_response = api.get_users_product(search=create_users_product['user_id'])
        products = json.loads(products_response.text)['users_products']

        assert 0 == len(products)


