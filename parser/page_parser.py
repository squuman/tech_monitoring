"Класс парсера сайта"
import requests
from bs4 import BeautifulSoup


class PageParser:
    url: str
    bs: BeautifulSoup

    def __init__(self, url):
        """
        Конструктор

        :param url:
        """
        self.url = url

    def _get_html(self):
        """
        Получение html-разметки страницы

        :return:
        """
        response = requests.get(self.url)

        if response.status_code != 200:
            raise Exception(f"Response is failed. Status code: {response.status_code}")

        return response.text

    def get_tags_href_from_search(self) -> list:
        """
        Получение списка ссылок из страницы поиска

        :return:
        """
        self.bs = BeautifulSoup(self._get_html(), 'html.parser')
        links_blocks = self.bs.findAll('a', {'class': 'model-short-title no-u'})

        return [tag['href'] for tag in links_blocks]

    def get_product_data(self) -> list:
        self.bs = BeautifulSoup(self._get_html(), 'html.parser')
        rows = self.bs.findAll('tr', {'class': 'priceElem'})
        price_list = []

        for row in rows:
            data = {
                'title': row.find('p').text,
                'price': str(row.find('a').text).replace('\xa0', ' '),
            }
            price_list.append(data)

        return price_list
