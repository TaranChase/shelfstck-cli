"""
Review Model

Creates a numeric review (1-5) for a book
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base



class Review(Base):
    """
    Stores a review made by user for a book

    A review is a numeric rating between 1 to 5 linked to a single book
    """
    
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    comment = Column(String)
    rating = Column(Integer)

    # ForeignKey will point to 'books.id' in books.py
    book_id = Column(Integer, ForeignKey('books.id'))

    book = relationship("Book", back_populates="reviews")

