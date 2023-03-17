"""
Создание таблицы продуктов
"""
from sql_app import Migration
from sql_app import Connector
from config import DATABASE


class CreateProductTableMigration(Migration):
    _connector = Connector(DATABASE['host'], DATABASE['user'], DATABASE['password'], DATABASE['database'])

    def up(self):
        self._connector.cursor.execute("CREATE TABLE products("
                                       "id INT PRIMARY KEY AUTO_INCREMENT,"
                                       "name VARCHAR(255),"
                                       "created_at DATETIME DEFAULT CURRENT_TIMESTAMP"
                                       ");")

    def down(self):
        self._connector.cursor.execute("DROP TABLE IF EXISTS products;")
