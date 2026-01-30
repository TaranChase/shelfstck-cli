# Shelfstck CLI

Shelfstck is a **command-line application** that allows users to manage their own personal bookshelf.

Users can:

- Add books
- Leave recommendations
- Track reading status
- Rate books

This project was initialized using the CLI + ORM template.

## Project Goal

This project was built to demonstrate and practice:

- Object Relational Mapping (ORM) with SQLALchemy
- CRUD Operations
- Command Line Interface (CLI) design
- Use of One-to-many database relationships
- The use of helpers and models to seperate logic, database work and user interaction in order to stay organized.

## Features (MVP)

- Add Books to the database
- View All Books in the database
- Recommend Books user has completed
- Add books reviews (1-5) rating
- View the ratings in star-based representation
- Remove a book with its related data

## Technologies Used

- Python3
- SQLAlchemy
- SQLite
- Pipenv

## How to Run the Application

1. Install dependencies

```bash
pipenv install
pipenv shell
```

2. Seed the Database (Optional - for testing ONLY)
   _Note:_ `debug.py` is a test file. Running multiple times will duplicate test data in the database. If re-running is required, delete `shelfstck-cli.db` first

```bash
python -m lib.debug
```

3. Start the CLI

```bash
python -m lib.cli
```

## Project Structure

shelfstck/
├── lib/
│ ├── cli.py
│ ├── debug.py
│ ├── helpers.py
│ └── models/
│ ├── init.py
│ ├── book.py
│ ├── recommendation.py
│ └── review.py
│
├── Pipfile
├── Pipfile.lock
├── README.md
└── shelfstck-cli.db

## File Descriptions

- **lib/cli.py** - Main CLI interface with menu system and user input handling
- **lib/helpers.py** - CRUD helper functions for books, reviews, and recommendations
- **lib/debug.py** - Database seeding and testing
- **lib/models/** - SQLAlchemy ORM models for Book, Review, and Recommendation

### Author

Taran Chase
