import sqlalchemy as sa

from app.controllers import Controller

from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import get_db

from app.models import ProductsPrice


class AverageController(Controller):
    def get_average(self, product_id: str = '', db: Session = Depends(get_db)):
        """
        Получение среднего арифметического цены продукта

        :param product_id: str
        :param db: Session
        :return:
        """

        products = db.query(ProductsPrice).filter(ProductsPrice.product_id == product_id).all()
        average = {}

        for product in products:
            if product.createdAt in average:
                average[product.createdAt]['all_price'] += product.price
                average[product.createdAt]['average'] += product.price
                average[product.createdAt]['count'] += 1
                average[product.createdAt]['average'] = \
                    average[product.createdAt]['all_price'] / average[product.createdAt]['count']
            else:
                average[product.createdAt] = {
                    "all_price": product.price,
                    "average": 0,
                    "count": 1
                }

        return average

