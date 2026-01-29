# Importing database requirements
from sqlalchemy import Column, Integer, String   
from . import Base


# Book Class 

class Book(Base):
    __tabletitle__ = "books"

    # Primary Key
    id = Column(Integer, primary_key=True)

    title = Column(String)
    author = Column(String)
    genre = Column(String)
    state = Column(String)

