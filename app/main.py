from fastapi import FastAPI
from app.database import Base, engine
from app.routers import books, authors, reviews

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bookstore API with PostgreSQL", version="1.0")

app.include_router(books.router)
app.include_router(authors.router)
app.include_router(reviews.router)

@app.get("/")
def root():
    return {"message": "Welcome to the PostgreSQL-powered Bookstore API 🚀"}
