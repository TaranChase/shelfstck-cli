# Creating tables

from models import Base, engine 
from models import Session, Book, Recommend, Review

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Database tables created.")


# Testing Models 

session = Session()
# Creating a book

book = Book(
    book_title = "Atomic Habits",
    book_author = "James Clear",
    book_genre = ["Self-help", "Non-fiction", "Therapy"],
    book_state = "reading"
)

session.add(book)
session.commit()


Base.metadata.create_all(engine)
