# lib/cli.py

"""
Command Line Interface for Shelfstck Application.

Handles user interaction while routing the menu options to their appropriate helper functions.
"""

from .helpers import (
    add_book, 
    view_all_books,
    add_recommendation,
    add_review,
    view_reviews,
    remove_book,
    exit_program
)

def menu():
    """
    Display main menu options to the user
    """
    print("\n Shelfstck CLI")
    print("Please select an option:")
    print("1. View ALL Books")
    print("2. Add a book")
    print("3. Add a recommendation")
    print("4. Add a review")
    print("5. View reviews")
    print("6. Remove a book")
    print("0. Exit")


def main():
    """
    The main app loop
    Will continuously display the menu and proces user input until user exits
    """
    
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            view_all_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            add_recommendation()
        elif choice == "4":
            add_review()
        elif choice == "5":
            view_reviews()
        elif choice == "6":
            remove_book()
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()
