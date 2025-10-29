from fastapi import FastAPI
from app.database import Base, engine
from app.routers import authors_router, books_router, reviews_router

# Import models package so metadata knows about tables
import app.models  # noqa: F401

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bookstore API - Simple")

app.include_router(authors_router)
app.include_router(books_router)
app.include_router(reviews_router)
