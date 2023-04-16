"""
Схема модели для продуктовой цены
"""
from datetime import datetime

from typing import List
from pydantic import BaseModel


class ProductsPriceBaseSchema(BaseModel):
    id: int | None = None
    product_id: int
    price: float
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ListProductsPriceResponse(BaseModel):
    status: str
    results: str
    users: List[ProductsPriceBaseSchema]
