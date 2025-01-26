from sqlalchemy import create_engine, text, Column, Integer, String
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import declarative_base

# Your database credentials and connection string
username = 'root'
password = 'root'
host = 'localhost'
port = '3306'  # Default MySQL port
database_name = 'femfinity'

# Create a connection string to MySQL without specifying a database
connection_string = f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/'

# Create an engine to connect to MySQL
engine = create_engine(connection_string)

# Try to create the database if it doesn't exist
try:
    with engine.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {database_name}"))
    print(f"Database '{database_name}' created or already exists.")
except OperationalError as e:
    print(f"Error occurred: {e}")

# Now that the database is created, connect to it
database_url = f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database_name}'
engine = create_engine(database_url)

# Now you can proceed with creating tables and other operations
Base = declarative_base()

# Define your models, e.g.:
# class User(Base):
#     ...

class User(Base):
    __tablename__ = 'users'  # Table name in the database
    
    user_id = Column(Integer, primary_key=True, autoincrement=True)  # Auto-increment primary key
    full_name = Column(String(100), nullable=False)  # Full name of the user
    email = Column(String(100), nullable=False, unique=True)  # Email address (unique)
    password = Column(String(255), nullable=False)  # Password (hashed or plain)


# Create the tables in the database
Base.metadata.create_all(engine)
