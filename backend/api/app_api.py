"""
Класс для работы с API приложения
"""
import json

import requests

from requests import Response

from api.apibase import ApiBase


class AppApi(ApiBase):
    """
    Класс для работы с методами API
    """

    users_url = 'http://127.0.0.1:8000/api/users/'
    products_url = 'http://127.0.0.1:8000/api/products/'

    def __init__(self):
        super().__init__()

    def create_user(self, data: dict) -> Response:
        """
        Создание пользователя

        :param data:
        :return:
        """
        response = requests.post(self.users_url, json=data)

        return response

    def get_users(self, limit=10, page=1, search: str = '') -> Response:
        """
        Получение списка пользователей

        :return:
        """
        response = requests.get(self.users_url + f"?limit={limit}&page={page}&search={search}")

        return response

    def get_user(self, id: str) -> Response:
        """
        Получение пользователя по id

        :param id:
        :return:
        """
        response = requests.get(self.users_url + id)

        return response

    def update_user(self, id: str, data: dict) -> Response:
        """
        Изменение пользователя

        :param id:
        :param data:
        :return:
        """
        response = requests.patch(self.users_url + id, json=data)

        return response

    def delete_user(self, id: str) -> Response:
        """
        Удаление пользователя

        :param id:
        :return:
        """
        response = requests.delete(self.users_url + id)

        return response

    def create_product(self, data: dict) -> Response:
        """
        Создание продукта

        :param data:
        :return:
        """
        response = requests.post(self.products_url, json=data)

        return response

    def get_products(self, limit=10, page=1, search: str = '') -> Response:
        """
        Получение списка пользователей

        :return:
        """
        response = requests.get(self.products_url + f"?limit={limit}&page={page}&search={search}")

        return response

    def get_product(self, id: str) -> Response:
        """
        Получение продукта по id

        :param id:
        :return:
        """
        response = requests.get(self.products_url + id)

        return response

    def update_product(self, id: str, data: dict) -> Response:
        """
        Изменение продукта

        :param id:
        :param data:
        :return:
        """
        response = requests.patch(self.products_url + id, json=data)

        return response

    def delete_product(self, id: str) -> Response:
        """
        Удаление продукта

        :param id:
        :return:
        """
        response = requests.delete(self.products_url + id)

        return response
