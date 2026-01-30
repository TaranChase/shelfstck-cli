"""
Recommendation Model

Creates a recommendation comment associated with a specific book user picks

"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base



class Recommend(Base):
    """
    Stores recommendation for a book.

    A recommendation belongs to a book and contains a short comment explaining why the book was recommended
    """
    
    __tablename__ = "recommendations"
    
    #Primary Key
    id = Column(Integer, primary_key=True)
    comment = Column(String)

    # ForeignKey will point to 'books.id' in books.py
    book_id = Column(Integer, ForeignKey('books.id'))

    book = relationship("Book", back_populates="recommendations")
