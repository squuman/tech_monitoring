"""
Описание рутов товаров
"""
from app.controllers import ProductController

from app.schemas import ProductBaseSchema
from fastapi import status, APIRouter

from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import get_db

product_router = APIRouter()
product_controller = ProductController()


@product_router.get('/')
def get_products(limit: int = 10, page: int = 1, search: str = '', db: Session = Depends(get_db)):
    return product_controller.get_products(limit, page, search, db)


@product_router.get('/{product_id}')
def get_product(product_id: str, db: Session = Depends(get_db)):
    return product_controller.get_product(product_id, db)


@product_router.post('/', status_code=status.HTTP_201_CREATED)
def create(payload: ProductBaseSchema, db: Session = Depends(get_db)):
    product_controller.create(payload, db)


@product_router.patch('/{product_id}')
def update(product_id, payload: ProductBaseSchema, db: Session = Depends(get_db)):
    product_controller.update_product(product_id, payload, db)


@product_router.delete('/{product_id}')
def delete(product_id: str, db: Session = Depends(get_db)):
    product_controller.delete_product(product_id, db)
