from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

# Define review class

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    comment = Column(String)
    rating = Column(Integer)

    # ForeignKey will point to 'books.id' in books.py
    book_id = Column(Integer, ForeignKey('books.id'))

    book = relationship("Book", back_populates="reviews")
