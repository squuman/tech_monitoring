from app.controllers import Controller

from app.models import Product
from app.schemas import ProductBaseSchema
from fastapi import HTTPException, status, Response

from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import get_db


class ProductController(Controller):
    def create(self, payload: ProductBaseSchema, db: Session = Depends(get_db)):
        new_product = Product(**payload.dict())
        db.add(new_product)
        db.commit()
        db.refresh(new_product)

        return {'status': 'success', 'product': new_product}

    def get_products(self, limit: int = 10, page: int = 1, search: str = '', db: Session = Depends(get_db)):
        skip = (page - 1) * limit

        products = db.query(Product).filter(Product.title.contains(search)).limit(limit).offset(skip).all()

        return {'status': 'success', 'results': len(products), 'products': products}

    def get_product(self, product_id: str, db: Session = Depends(get_db)):
        product_query = db.query(Product).filter(Product.id == product_id)
        db_product = product_query.first()

        if not db_product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'No note with this id: {product_id} found')

        return db_product

    def update_product(self, product_id, payload: ProductBaseSchema, db: Session = Depends(get_db)):
        product_query = db.query(Product).filter(Product.id == product_id)
        db_product = product_query.first()

        if not db_product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'No note with this id: {product_id} found')

        update_data = payload.dict(exclude_unset=True)
        product_query.filter(Product.id == product_id).update(update_data, synchronize_session=False)

        db.commit()
        db.refresh(db_product)

        return {'status': 'success', 'product': db_product}

    def delete_product(self, product_id: str, db: Session = Depends(get_db)):
        product_query = db.query(Product).filter(Product.id == product_id)
        db_product = product_query.first()

        if not db_product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'No note with this id: {product_id} found')

        product_query.delete(synchronize_session=False)
        db.commit()

        return Response(status_code=status.HTTP_204_NO_CONTENT)
