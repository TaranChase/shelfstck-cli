# lib/cli.py

from helpers import (
    add_book, 
    view_books,
    add_recommendation,
    add_review,
    exit_program
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            add_recommendation()
        elif choice == "4":
            add_review()
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice. Please try again.")

def menu():
    print("\n Shelfstck CLI")
    print("Please select an option:")
    print("1. Add a book")
    print("2. View all books")
    print("3. Add a recommendation")
    print("4. Add a review")
    print("0. Exit")


if __name__ == "__main__":
    main()
