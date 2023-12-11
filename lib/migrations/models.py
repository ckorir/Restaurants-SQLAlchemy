# Import necessary SQLAlchemy modules
from sqlalchemy import create_engine, inspect
from sqlalchemy import ForeignKey, Table, Column, Integer, String
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a SQLAlchemy database engine
engine = create_engine('sqlite:///restaurant.db')
inspector = inspect(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create a base class for declarative models
Base = declarative_base()

# Define a many-to-many relationship table between restaurants and customers
restaurant_customer = Table(
    'restaurants_customers',
    Base.metadata,
    Column('restaurant_id', ForeignKey('restaurants.id'), primary_key=True),
    Column('customer_id', ForeignKey('customers.id'), primary_key=True),
    extend_existing=True,
)

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(Integer())

