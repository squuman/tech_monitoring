from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine

from app.models.user import Base

from app.routes.user_routes import user_router

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


@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI, fuckin' slave!"}