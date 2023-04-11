import random
import string


def get_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_products(count=1):
    """
    Генерация данных пользователей

    :param count:
    :return:
    """
    return [{
        "title": get_random_string(),
        "price": random.randint(0, 1000) * 1.0,
    } for i in range(count)]
