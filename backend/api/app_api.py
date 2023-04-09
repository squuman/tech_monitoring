"""
Класс для работы с API приложения
"""
import json

import requests

from requests import Response

from api.apibase import ApiBase


class AppApi(ApiBase):
    """

    """
    url = 'http://127.0.0.1:8000/api/users/'

    def __init__(self):
        super().__init__()

    def create_user(self, data: dict) -> Response:
        """
        Создание пользователя

        :param data:
        :return:
        """
        response = requests.post(self.url, json=data)

        return response

    def get_users(self, limit=10, page=1, search: str = '') -> Response:
        """
        Получение списка пользователей

        :return:
        """
        response = requests.get(self.url + f"?limit={limit}&page={page}&search={search}")

        return response

    def get_user(self, id: str) -> Response:
        """
        Получение пользователя по id

        :param id:
        :return:
        """
        response = requests.get(self.url + id)

        return response

    def update_user(self, id: str, data: dict) -> Response:
        """
        Изменение пользователя

        :param id:
        :param data:
        :return:
        """
        response = requests.patch(self.url + id, json=data)

        return response

    def delete_user(self, id: str) -> Response:
        """
        Удаление пользователя

        :param id:
        :return:
        """
        response = requests.delete(self.url + id)

        return response
