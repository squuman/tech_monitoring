"""
Схема модели для продукта пользователя
"""
from datetime import datetime
from typing import List
from pydantic import BaseModel


class UsersProductBaseSchema(BaseModel):
    id: int | None = None
    user_id: int
    product_id: int
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ListUsersProductBaseSchemaResponse(BaseModel):
    status: str
    results: str
    users: List[UsersProductBaseSchema]
