from app.database import Base
from sqlalchemy import TIMESTAMP, Column, String, Integer, Float, ForeignKey, DATE
from sqlalchemy.sql import func


class ProductsPrice(Base):
    __tablename__ = 'products_price'
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    storage = Column(String, nullable=False)
    product_id = Column(ForeignKey('products.id'), nullable=False)
    createdAt = Column(DATE,
                       nullable=False, server_default=func.now())
    updatedAt = Column(DATE,
                       default=None, onupdate=func.now())
