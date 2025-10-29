from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
import uuid

# ---------- Authors ----------
def create_author(db: Session, author_in: schemas.AuthorCreate) -> models.Author:
    db_obj = models.Author(name=author_in.name)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_author(db: Session, author_id: str):
    try:
        uid = uuid.UUID(author_id)
    except Exception:
        return None
    return db.query(models.Author).filter(models.Author.id == uid).first()

def list_authors(db: Session, skip: int = 0, limit: int = 100) -> List[models.Author]:
    return db.query(models.Author).offset(skip).limit(limit).all()

# ---------- Books ----------
def create_book(db: Session, book_in: schemas.BookCreate) -> models.Book:
    db_obj = models.Book(title=book_in.title, author_id=book_in.author_id)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_book(db: Session, book_id: str):
    try:
        uid = uuid.UUID(book_id)
    except Exception:
        return None
    return db.query(models.Book).filter(models.Book.id == uid).first()

def list_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()

# ---------- Reviews ----------
def create_review(db: Session, review_in: schemas.ReviewCreate) -> models.Review:
    db_obj = models.Review(content=review_in.content, rating=review_in.rating, book_id=review_in.book_id)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def list_reviews_for_book(db: Session, book_id: str):
    try:
        uid = uuid.UUID(book_id)
    except Exception:
        return []
    return db.query(models.Review).filter(models.Review.book_id == uid).all()
