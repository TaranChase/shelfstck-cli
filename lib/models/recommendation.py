from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

# Recommendation class

class Recommend(Base):
    __tablename__ = "recommendations"
    
    #Primary Key
    id = Column(Integer, primary_key=True)
    note = Column(String)

    # ForeignKey will point to 'books.id' in books.py
    book_id = Column(Integer, ForeignKey('books.id'))

    book = relationship("Book", back_populates="recommendations")
