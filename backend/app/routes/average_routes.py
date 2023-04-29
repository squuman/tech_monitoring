from app.controllers import AverageController
from app.schemas import ProductsPriceBaseSchema

from fastapi import status, APIRouter

from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import get_db

average_router = APIRouter()
average_controller = AverageController()


@average_router.get('/{product_id}')
def get_average(product_id, db: Session = Depends(get_db)):
    return average_controller.get_average(product_id, db)