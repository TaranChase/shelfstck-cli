# Creating tables

from models import Base, engine 
from models import Session, Book, Recommend, Review

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Database tables created.")


session = Session()

Base.metadata.create_all(engine)
