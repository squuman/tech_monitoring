from app.controllers import Controller

from app.models import User
from app.schemas import UserBaseSchema
from fastapi import HTTPException, status, Response

from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import get_db


class UserController(Controller):
    def create(self, payload: UserBaseSchema, db: Session = Depends(get_db)):
        new_user = User(**payload.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return {'status': 'success', 'user': new_user}

    def get_users(self, limit: int = 10, page: int = 1, search: str = '', db: Session = Depends(get_db)):
        skip = (page - 1) * limit

        users = db.query(User).filter(User.login.contains(search)).limit(limit).offset(skip).all()

        return {'status': 'success', 'results': len(users), 'users': users}

    def get_user(self, user_id: str, db: Session = Depends(get_db)):
        user_query = db.query(User).filter(User.id == user_id)
        db_user = user_query.first()

        if not db_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'No note with this id: {user_id} found')

        return db_user

    def update_user(self, user_id, payload: UserBaseSchema, db: Session = Depends(get_db)):
        user_query = db.query(User).filter(User.id == user_id)
        db_user = user_query.first()

        if not db_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'No note with this id: {user_id} found')

        update_data = payload.dict(exclude_unset=True)
        user_query.filter(User.id == user_id).update(update_data, synchronize_session=False)

        db.commit()
        db.refresh(db_user)

        return {'status': 'success', 'user': db_user}

    def delete_user(self, user_id: str, db: Session = Depends(get_db)):
        user_query = db.query(User).filter(User.id == user_id)
        db_user = user_query.first()

        if not db_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'No note with this id: {user_id} found')

        user_query.delete(synchronize_session=False)
        db.commit()

        return Response(status_code=status.HTTP_204_NO_CONTENT)
