import random
import string


def get_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_users(count=1):
    """
    Генерация данных пользователей

    :param count:
    :return:
    """
    return [{
        "login": get_random_string(),
        "name": get_random_string(),
        "password": get_random_string(),
    } for i in range(count)]
