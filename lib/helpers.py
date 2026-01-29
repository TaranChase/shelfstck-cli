# lib/helpers.py

from models import Session, Book, Recommend, Review

session = Session()

# Add Book Logic 

def add_book():
    title = input("Title: ")
    author = input("Author: ")
    genre = input("Genre: ")
    state = input("Status (read/currently reading/completed)")

    if not title or not author:
        print("Invalid. Please enter a Book Title and Author.")
        return
    
    book = Book(title=title, author=author, genre=genre, state=state)
    session.add(book)
    session.commit()

    print("Your book has been added successfully!")
                
def helper_1():
    print("Performing useful function#1.")


# View all books 

def view_all_books():
    books = session.query(Book).all()

    if not books:
        print("Sorry! No books were found here!")
        return
    
    for book in books:
        print(f"{book.id}: {book.title} by {book.author}")


# Add recommendations 

def add_recommendation():
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

# Add review 

def add_review():
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

# Exiting programm

def exit_program():
    print("Goodbye!")
    session.close()
    exit()
