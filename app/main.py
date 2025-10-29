from fastapi import FastAPI
from app.database import Base, engine
from app.routers import authors_router, books_router, reviews_router

import app.models  

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bookstore API - Simple")

app.include_router(authors_router)
app.include_router(books_router)
app.include_router(reviews_router)

