"""
Initializing models package

This configures the database and ORM for the Shelfstck CLI Application 
It includes the SQLAlchemy engine, session maker, and the Declarative Base class used by all the models

The model classes are imported here to ensure that they are registered with the SQLAlchemy metadata.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine("sqlite:///shelfstck-cli.db")
Session = sessionmaker(bind=engine)

class Base (DeclarativeBase):
    """
    The Base class for all SQLAlchemy ORM Models
    """
    pass


# Importing models to register with SQLAlchemy
from .book import Book
from .recommendation import Recommend
from .review import Review

