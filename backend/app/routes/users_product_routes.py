"""
Описание рутов товаров
"""
from app.controllers import UsersProductController

from app.schemas import UsersProductBaseSchema
from fastapi import status, APIRouter

from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import get_db

users_product_router = APIRouter()
users_product_controller = UsersProductController()


@users_product_router.get('/')
def get_users_products(limit: int = 10, page: int = 1, search: str = '', db: Session = Depends(get_db)):
    return users_product_controller.get_users_products(limit, page, db)


@users_product_router.post('/', status_code=status.HTTP_201_CREATED)
def create(payload: UsersProductBaseSchema, db: Session = Depends(get_db)):
    users_product_controller.create_users_product(payload, db)


@users_product_router.delete('/{users_product_id}')
def delete(users_product_id: str, db: Session = Depends(get_db)):
    users_product_controller.delete_users_product(users_product_id, db)
