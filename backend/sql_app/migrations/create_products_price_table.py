"""
Создание таблицы цен продуктов
"""
from sql_app import Migration
from sql_app import Connector
from config import DATABASE


class CreateProductsPriceTableMigration(Migration):
    _connector = Connector(DATABASE['host'], DATABASE['user'], DATABASE['password'], DATABASE['database'])

    def up(self):
        self._connector.cursor.execute("CREATE TABLE products_price("
                                       "id INT PRIMARY KEY AUTO_INCREMENT,"
                                       "product_id INT,"
                                       "price FLOAT,"
                                       "FOREIGN KEY (product_id) REFERENCES products(id),"
                                       "created_at DATETIME DEFAULT CURRENT_TIMESTAMP"
                                       ");")

    def down(self):
        self._connector.cursor.execute("DROP TABLE IF EXISTS products_price;")
