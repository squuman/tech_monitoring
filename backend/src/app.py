"""
Инициализация приложения
Описание путей
"""
from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get('/ping')
def ping_pong():
    """
    Test connection with API

    :return:
    """
    return {'value': 'pong'}