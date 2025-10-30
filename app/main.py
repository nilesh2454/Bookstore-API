from fastapi import FastAPI
from app.database import Base, engine
from app.models import author, book, review
from app.routers import authors, books, reviews

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bookstore API")

# ✅ Directly include routers, without .router
app.include_router(authors)
app.include_router(books)
app.include_router(reviews)

@app.get("/")
def root():
    return {"message": "Welcome to the Bookstore API!"}
