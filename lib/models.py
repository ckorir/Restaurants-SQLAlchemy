# Import necessary SQLAlchemy modules
from sqlalchemy import create_engine, inspect
from sqlalchemy import ForeignKey, Table, Column, Integer, String
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a SQLAlchemy database engine
engine = create_engine('sqlite:///restaurbase.db')
inspector = inspect(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create a base class for declarative models
Base = declarative_base()