# lib/helpers.py

from models import Session, Book, Recommend, Review

session = Session()

# Add Book Logic 

def add_book():
    book_title = input("Title: ")
    book_author = input("Author: ")
    book_genre = input("Genre: ")
    book_state = input("Status (read/currently reading/completed)")

    if not book_title or not book_author:
        print("Invalid. Please enter a Book Title and Author.")
        return
    
    book = Book(book_title=book_title, book_author=book_author, book_genre=book_genre, book_state=book_state)
    session.add(Book)
    session.commit()

    print("Your book has been added successfully!")
                
def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()
