import json
import time

import pytest
import allure


@allure.title("Создание продуктовой цены")
def test_get_products_price(api, create_products_price):
    with allure.step("Отправка запроса для получения продуктовой цены"):
        product = json.loads(api.get_products_price(search=create_products_price['product_id']).text)['products'][0]

        assert create_products_price['price'] == product['price']
        assert create_products_price['product_id'] == product['product_id']


@allure.title("Удаление продуктовой цены")
def test_delete_products_price(api, create_products_price):
    with allure.step("Отправка запроса для удаления продуктовой цены"):
        api.delete_products_price(str(create_products_price['id']))
        products = json.loads(api.get_products_price(search=create_products_price['id']).text)['products']

        assert 0 == len(products)
