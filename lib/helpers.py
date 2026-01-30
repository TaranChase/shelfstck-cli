# lib/helpers.py


"""
Helper functionc created for my Shelfstck CLI Application.

Contains all CRUD - related operations that interact with the database using SQLAlchemy sessions.
The functions are called by the CLI Menu to perform certain action e.g adding books, reviewing books, recommendations, and removing records.
"""


from models import Session, Book, Recommend, Review
session = Session()



def add_book():

    """
    Will prompt a user for book details such as book title, author, genre and the status. It then saves the new book to the database.
    """

    title = input("Title: ")
    author = input("Author: ")
    genre = input("Genre: ")
    state = input("Status: (want to read/currently reading/completed)")

    if not title or not author:
        print("Invalid. Please enter a Book Title and Author.")
        return
    
    book = Book(title=title, author=author, genre=genre, state=state)
    session.add(book)
    session.commit()

    print("Your book has been added successfully!")
                
def helper_1():
    print("Performing useful function#1.")



def view_all_books():
    """
    Displays all books stored in the database.
    """
    books = session.query(Book).all()

    if not books:
        print("Sorry! No books were found here!")
        return
    
    for book in books:
        print(f"{book.id}: {book.title} by {book.author}")



def add_recommendation():
    """
    The user selects a book by ID and provides a recommendation comment.
    """

    book_id = input("Enter ID: ")

    book = session.query(Book).filter_by(id=book_id).first()

    if not book:
        print("Sorry. Book not found.")
        return 
    
    comment = input("Recommendation: ")

    recommendation = Recommend(comment=comment, book=book)
    session.add(recommendation)
    session.commit()

    print("Your recommendation has been successfully added!")


def add_review():
    """
    Adds a numerical rating (1-5) to a book the user selects.
    """

    book_id = input("Book ID: ")

    book = session.query(Book).filter_by(id=book_id).first()

    if not book:
        print("Sorry. Book not found.")
        return
    
    rating = input("Rating (1-5): ")

    if not rating.isdigit() or not (1 <= int(rating) <= 5):
        print("Invalid. Rating must be an Integer an must be between 1 and 5.")
        return 
    
    review = Review(rating=int(rating), book=book)
    session.add(review)
    session.commit()

    print("Your review was added.")




def rating_to_stars(rating):
    """
    Converts the numeric rating given in add_review into a visual star representation

    """
    return "⭐" * rating + "☆" * (5 - rating)



def view_reviews():
    """
    Displays all book reviews in the star based format
    """

    reviews = session.query(Review).all()

    if not reviews:
        print("Sorry. No reviews found.")

    for review in reviews:
        stars = rating_to_stars(review.rating)
        print(f"{review.book.title} - {stars}")


def remove_book():
    """
    Deletes a book from the database
    """

    book_id = input("Book ID: ")

    book = session.query(Book).filter_by(id=book_id).first()

    if not book:
        print("Sorry. Book not found.")
        return
    
    session.delete(book)
    session.commit()

    print("Book successfully removed.")


def exit_program():
    """
    Exits the application and closes the database session safely
    """
    
    print("Goodbye!")
    session.close()
    exit()
