from app.database import Base
from sqlalchemy import TIMESTAMP, Column, String, Integer, ForeignKey
from sqlalchemy.sql import func


class UsersProduct(Base):
    __tablename__ = 'users_products'
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("users.id"))
    product_id = Column(ForeignKey("products.id"))
    createdAt = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=func.now())
    updatedAt = Column(TIMESTAMP(timezone=True),
                       default=None, onupdate=func.now())
