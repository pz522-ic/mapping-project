from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from module_class import Base  # where Base, Module, and Keyword are defined

# database engine
engine = create_engine('sqlite:///modules.db')

# session
Session = sessionmaker(bind=engine)
session = Session()


# Base.metadata.create_all(engine)  
