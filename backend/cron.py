import json
import requests
from datetime import datetime

from parser.parser import PageParser

base_url = 'https://n-katalog.ru'
api_url = 'http://127.0.0.1:8000/api/'


def app():
    # получаем список продуктов пользователей
    get_products_response = requests.get(api_url + 'products')

    if get_products_response.status_code != 200:
        raise Exception(get_products_response.text)

    for product in json.loads(get_products_response.text)['products']:
        # Получаем данные продукта

        search_parser = PageParser(base_url + "/search?keyword=" + product['title'].replace(" ", "+"))

        for path in search_parser.get_tags_href_from_search():
            # Записываем в бд данные продукта
            for data in PageParser(base_url + path).get_product_data():
                if data is None:
                    continue

                print({
                    "product_id": product['id'],
                    "price": data['price'],
                })

                requests.post(api_url + 'products_price/', json={
                    "product_id": product['id'],
                    "price": data['price'].replace(' руб', ''),
                })


if __name__ == '__main__':
    app()
