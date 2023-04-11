import pytest

import json

from api.app_api import AppApi
from data import generate_users


@pytest.fixture
def api():
    return AppApi()


@pytest.fixture
def create_user():
    data = generate_users()[0]
    api = AppApi()

    api.create_user(data)
    response = api.get_users(search=data['name'])
    user = json.loads(response.text)['users'][0]

    try:
        yield user
    finally:
        api.delete_user(str(user['id']))


@pytest.fixture
def delete_user(user_id: str):
    api = AppApi()

    try:
        pass
    finally:
        api.delete_user(user_id)
