# Importing database requirements
from sqlalchemy import Column, Integer, String   
from . import Base
from sqlalchemy.orm import relationship


# Book Class 

class Book(Base):
    __tablename__ = "books"

    # Primary Key
    id = Column(Integer, primary_key=True)

    title = Column(String)
    author = Column(String)
    genre = Column(String)
    state = Column(String)

    
    # Storing a new book in SQLite 
    def create(self, session):
        session.add(self)
        session.commit()


    # View all books
    @classmethod
    def all_books(cls, session):
        return session.query(cls).all()
    

    # View specific books using their specific id
    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()
    
    # Deleting/Removing a book 
    def delete(self, session):
        session.delete(self)
        session.commit()
    
    # Updating Book to complete and sync the relationship
    recommendations = relationship("Recommend", back_populates="book")
    reviews = relationship("Review", back_populates="book")
