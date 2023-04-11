"""
Описание рутов товаров
"""
from app.controllers import ProductsPriceController

from app.schemas import ProductsPriceBaseSchema
from fastapi import status, APIRouter

from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import get_db

products_price_router = APIRouter()
products_price_controller = ProductsPriceController()


@products_price_router.get('/')
def get_products_prices(limit: int = 10, page: int = 1, search: str = '', db: Session = Depends(get_db)):
    return products_price_controller.get_products_price(limit, page, search, db)


@products_price_router.post('/', status_code=status.HTTP_201_CREATED)
def create(payload: ProductsPriceBaseSchema, db: Session = Depends(get_db)):
    products_price_controller.create(payload, db)


@products_price_router.patch('/{products_price_id}')
def update(products_price_id, payload: ProductsPriceBaseSchema, db: Session = Depends(get_db)):
    products_price_controller.update_products_price(products_price_id, payload, db)


@products_price_router.delete('/{products_price_id}')
def delete(products_price_id: str, db: Session = Depends(get_db)):
    products_price_controller.delete_products_price(products_price_id, db)
