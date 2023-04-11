import pytest

import json

from api.app_api import AppApi
from data import generate_products


@pytest.fixture
def api():
    return AppApi()


@pytest.fixture
def create_product():
    data = generate_products()[0]
    api = AppApi()

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
