"""
Database Testing


Creates database tables and inserts the test data for model relationship testing and overall functionality
"""

from .models import Base, engine, Session, Book, Recommend, Review

if __name__ == "__main__":
    """
    Creates all the database tables as well as seeds the initial test data
    """

    Base.metadata.create_all(engine)
    print("Database tables created.")

    # Testing Models 
    session = Session()

    # Creating a book (if they do not already exist)

    # Check if books already exist
    existing_books = session.query(Book).count()

    if existing_books == 0:
        book_1 = Book(
            title = "Atomic Habits",
            author = "James Clear",
            genre = "Self-help, Non-Fiction, Therapy",
            state = "currently reading"
        )

        book_2 = Book(
            title = "Pride and Prejudice",
            author = "Jane Austen",
            genre = "Historical Drama, Romance",
            state = "completed"
        )

        book_3 = Book(
            title = "The Hobbit",
            author = "J.R.R Tolkein",
            genre = "Adventure",
            state = "want to read"
        )

        book_4 = Book(
            title = "Frankeinstein",
            author = "Mary Wollstonecraft Shelley",
            genre = "Horror, Thriller",
            state = "completed"
        )

        book_5 = Book(
            title = "Stalin's War: A New History of World War II",
            author = "Sean McMeekin",
            genre = "History",
            state = "want to read"
        )

        session.add_all([book_1, book_2, book_3, book_4, book_5])
        session.commit()
        print("New books added to database.")
    else:
        print("Books already exist in database, skipping creation.")


    # Query books from database for use in recommendations and reviews

    book_2 = session.query(Book).filter_by(title="Pride and Prejudice").first()
    book_4 = session.query(Book).filter_by(title="Frankeinstein").first()


    # Adding a book recommendation 

    # Pride and Prejudice
    rc1 = Recommend(
        comment = "Pure period drama. What a classic!",
        book = book_2
    )

    # Frankeinstein
    rc2 = Recommend(
        comment = "Maddness. Terrifying, Gruseome yet a rather emotional text.",
        book = book_4
    )

    session.add_all([rc1, rc2])
    session.commit()

    print("\nRecommendations:")
    for recomm in [rc1, rc2]:
        print("-", recomm.comment)


    # Testing Reviews
    rv1 = Review (
        rating = 4,
        book = book_2
    )

    rv2 = Review(
        rating = 2,
        book = book_4
    )

    session.add_all([rv1, rv2])
    session.commit()

    print("\nRating:")
    for r in [rv1, rv2]:
        print("-", r.rating)


    # Querying Books 

    books = session.query(Book).all()

    for b in books:
        print(b.id, b.title, b.author, f"{b.state}")

