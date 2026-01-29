# Creating tables

from models import Base, engine, Session, Book, recommendation, review

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Database tables created.")


# Testing Models 

session = Session()
# Creating a book

book = Book(
    title = "Atomic Habits",
    author = "James Clear",
    genre = "Self-help, Non-Fiction, Therapy",
    state = "reading"
)

session.add(book)
session.commit()

# Querying Books 

books = session.query(Book).all()

for b in books:
    print(b.id, b.title, b.author)




