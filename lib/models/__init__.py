from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///shelfstck-cli.db")
Session = sessionmaker(bindengine)
Base = declarative_base()

