"""
Схема данных для продукта
"""
from datetime import datetime
from typing import List
from pydantic import BaseModel


class ProductBaseSchema(BaseModel):
    id: int | None = None
    title: str
    price: float
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ListProductResponse(BaseModel):
    status: str
    results: str
    users: List[ProductBaseSchema]
