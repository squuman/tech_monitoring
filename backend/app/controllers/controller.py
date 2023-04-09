from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import get_db


class Controller:
    db: Session = Depends(get_db)
