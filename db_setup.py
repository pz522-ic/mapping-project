from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base  # Ensure this matches the file where Base, Module, and Keyword are defined

# database engine
engine = create_engine('sqlite:///modules.db')

# session
Session = sessionmaker(bind=engine)
session = Session()


# Base.metadata.create_all(engine)  # Uncomment if you need to ensure tables are created
