from app.controllers import Controller

from app.models import UsersProduct
from app.schemas import UsersProductBaseSchema
from fastapi import HTTPException, status, Response

from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import get_db


class UsersProductController(Controller):
    def create_users_product(self, payload: UsersProductBaseSchema, db: Session = Depends(get_db)):
        new_user = UsersProduct(**payload.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return {'status': 'success', 'user': new_user}

    def get_users_products(self, limit: int = 10, page: int = 1, db: Session = Depends(get_db)):
        skip = (page - 1) * limit

        users_products = db.query(UsersProduct).limit(limit).offset(
            skip).all()

        return {'status': 'success', 'results': len(users_products), 'users_products': users_products}

    def delete_users_product(self, user_id: str, db: Session = Depends(get_db)):
        user_query = db.query(UsersProduct).filter(UsersProduct.id == user_id)
        db_user = user_query.first()

        if not db_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'No note with this id: {user_id} found')

        user_query.delete(synchronize_session=False)
        db.commit()

        return Response(status_code=status.HTTP_204_NO_CONTENT)
