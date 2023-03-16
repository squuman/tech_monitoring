from parser import PageParser


def app():
    base_url = 'https://n-katalog.ru'
    path = '/search?keyword=rtx+3060'

    search_parser = PageParser(base_url + path)
    product_data = []

    for path in search_parser.get_tags_href_from_search():
        page_parser = PageParser(base_url + path)
        product_data.append({
            "path": path,
            "data": page_parser.get_product_data()
        })

    print(product_data)


if __name__ == '__main__':
    app()
