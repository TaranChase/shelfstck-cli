# Creating tables

from models import Base, engine, Session, Book, Recommend, Review
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
    print(b.id, b.title, b.author, b.state)



# Adding a book recommendation 

book_recommendation = Recommend(
    comment = "This book changed my view on self sabotage and building good habits. Highly recommend!",
    book_id = book.id
)

session.add(book_recommendation)
session.commit()

print("Recommendation:")
for recomm in book.recommendations:
    print(recomm.comment)


  # Testing Reviews

    review = Review(
        rating = 8,
        book_id = book.id
    )

    session.add(review)
    session.commit()

    print("Rating:")
    for r in book.reviews:
        print(r.rating)