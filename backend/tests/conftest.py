import random

import pytest

import logging
import json

from api.app_api import AppApi
from data import generate_users, generate_products

api = AppApi()


@pytest.fixture
def api():
    return AppApi()


@pytest.fixture
def create_user():
    """
    Фикстура создания пользователя

    :return:
    """
    api = AppApi()
    data = generate_users()[0]

    api.create_user(data)
    response = api.get_users(search=data['login'])
    user = json.loads(response.text)['users'][0]

    try:
        yield user
    finally:
        api.delete_user(str(user['id']))


@pytest.fixture
def delete_user(user_id: str):
    """
    Удаление пользователя

    :param user_id:
    :return:
    """
    api = AppApi()

    try:
        pass
    finally:
        api.delete_user(user_id)


@pytest.fixture
def create_product():
    """
    Создание продукта

    :return:
    """
    api = AppApi()
    data = generate_products()[0]

    api.create_product(data)
    response = api.get_products(search=data['title'])
    product = json.loads(response.text)['products'][0]

    try:
        yield product
    finally:
        api.delete_product(str(product['id']))


@pytest.fixture
def delete_product(product_id: str):
    api = AppApi()

    try:
        pass
    finally:
        api.delete_product(product_id)


@pytest.fixture
def create_users_product():
    """
    Привязка продукта к пользователю

    :return:
    """
    api = AppApi()

    user_data = generate_users()[0]
    product_data = generate_products()[0]

    # создание пользователя
    api.create_user(user_data)
    user_response = api.get_users(search=user_data['login'])
    user = json.loads(user_response.text)['users'][0]

    # создание продукта
    api.create_product(product_data)
    product_response = api.get_products(search=product_data['title'])
    product = json.loads(product_response.text)['products'][0]

    # привязка продукта к пользователю
    api.create_users_product(user['id'], product['id'])
    users_product_response = api.get_users_product(search=user['id'])

    users_product = json.loads(users_product_response.text)['users_products'][0]

    try:
        yield users_product
    finally:
        api.delete_users_product(str(users_product['id']))


@pytest.fixture
def create_products_price():
    """
    Создание продуктовых цен

    :return:
    """

    api = AppApi()
    product_data = generate_products()[0]

    api.create_product(product_data)
    product_response = api.get_products(search=product_data['title'])
    product = json.loads(product_response.text)['products'][0]

    api.create_products_price(product['id'], str(random.randint(0, 10) * 1.0))
    products_price = json.loads(api.get_products_price(search=product['id']).text)['products']

    try:
        yield products_price[0]
    finally:
        api.delete_products_price(str(products_price[0]['id']))