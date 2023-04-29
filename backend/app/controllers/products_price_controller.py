from app.controllers import Controller

from app.models import ProductsPrice, Product
from app.schemas import ProductsPriceBaseSchema
from fastapi import HTTPException, status, Response

from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import get_db


class ProductsPriceController(Controller):
    def create(self, payload: ProductsPriceBaseSchema, db: Session = Depends(get_db)):
        new_product = ProductsPrice(**payload.dict())
        db.add(new_product)
        db.commit()
        db.refresh(new_product)

        return {'status': 'success', 'product': new_product}

    def get_products_price(self, limit: int = 10, page: int = 1, search: str = '', db: Session = Depends(get_db)):
        skip = (page - 1) * limit

        products = db.query(ProductsPrice).filter(ProductsPrice.product_id == search).limit(limit).offset(skip).all()
        products_count = db.query(ProductsPrice).filter(Product.id == search).count()

        return {
            'status': 'success',
            'results': len(products),
            'count': products_count,
            'products': products
        }

    def update_products_price(self, product_id, payload: ProductsPriceBaseSchema, db: Session = Depends(get_db)):
        product_query = db.query(ProductsPrice).filter(ProductsPrice.id == product_id)
        db_product = product_query.first()

        if not db_product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'No note with this id: {product_id} found')

        update_data = payload.dict(exclude_unset=True)
        product_query.filter(ProductsPrice.id == product_id).update(update_data, synchronize_session=False)

        db.commit()
        db.refresh(db_product)

        return {'status': 'success', 'product': db_product}

    def delete_products_price(self, product_id: str, db: Session = Depends(get_db)):
        product_query = db.query(ProductsPrice).filter(ProductsPrice.id == product_id)
        db_product = product_query.first()

        if not db_product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'No note with this id: {product_id} found')

        product_query.delete(synchronize_session=False)
        db.commit()

        return Response(status_code=status.HTTP_204_NO_CONTENT)
