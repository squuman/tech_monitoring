"""
Описание рутов пользователей
"""
from app.controllers import UserController

from app.schemas import UserBaseSchema
from fastapi import status, APIRouter

from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import get_db

user_router = APIRouter()
user_controller = UserController()


@user_router.get('/')
def get_users(limit: int = 10, page: int = 1, search: str = '', db: Session = Depends(get_db)):
    return user_controller.get_users(limit, page, search, db)


@user_router.get('/{user_id}')
def get_user(user_id: str, db: Session = Depends(get_db)):
    return user_controller.get_user(user_id, db)


@user_router.post('/', status_code=status.HTTP_201_CREATED)
def create(payload: UserBaseSchema, db: Session = Depends(get_db)):
    user_controller.create(payload, db)


@user_router.patch('/{user_id}')
def update(user_id, payload: UserBaseSchema, db: Session = Depends(get_db)):
    user_controller.update_user(user_id, payload, db)


@user_router.delete('/{user_id}')
def delete(user_id: str, db: Session = Depends(get_db)):
    user_controller.delete_user(user_id, db)
