from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine

from app.models.user import Base

from app.routes import user_router, product_router, users_product_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, tags=['User'], prefix='/api/users')
app.include_router(product_router, tags=['Product'], prefix='/api/products')
app.include_router(users_product_router, tags=['UsersProduct'], prefix='/api/users_product')


@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI, fuckin' slave!"}