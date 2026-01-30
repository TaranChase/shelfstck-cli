"""
Book Model

Defines Book class and represents its database
"""


from sqlalchemy import Column, Integer, String   
from . import Base
from sqlalchemy.orm import relationship


# Book Class 

class Book(Base):
    """
    Represents a book in the Shelfstck application

    Book stores the basic necessary data needed i.e title, auhor, genre and state.
    It maintains relationships between both recommendations and reviews database.
    """
    __tablename__ = "books"

    # COLUMNS

    # Primary Key
    id = Column(Integer, primary_key=True)

    title = Column(String)
    author = Column(String)
    genre = Column(String)
    state = Column(String)

    # CRUD Methods 

    def create(self, session):
        """
        Current Book instance is saved to database

        """

        session.add(self)
        session.commit()


    @classmethod
    def all_books(cls, session):
        """
        Returns all books stored in the database

        """
        return session.query(cls).all()
    

    @classmethod
    def find_by_id(cls, session, id):
        """
        Finds a book from the database by its unique ID
        
        :param session: Active SQLAlchemy session
        :param id: Unique ID of a book to be retrieved from database
        """

        return session.query(cls).filter_by(id=id).first()
    

    def delete(self, session):
        """
        Deletes and Removes the current Book instance from the database

        The associated recommendations and reviews are also deleted
        """

        session.delete(self)
        session.commit()
    

    # RELATIONSHIPS 

    recommendations = relationship("Recommend", back_populates="book", cascade="all, delete")
    reviews = relationship("Review", back_populates="book", cascade="all, delete")

  