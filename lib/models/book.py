# Importing database requirements
from sqlalchemy import Column, Integer, String   
from . import Base


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

    