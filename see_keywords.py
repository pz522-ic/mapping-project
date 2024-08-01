from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from module_class import Keyword, Base

# Database setup
DATABASE_URL = 'sqlite:///modules.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Query all keywords
keywords = session.query(Keyword).all()

# Print out all keywords
for keyword in keywords:
    print(f"Keyword ID: {keyword.id}, Keyword: {keyword.keyword}")

# Close session
session.close()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from module_class import Module, Keyword, Base

# Database setup
DATABASE_URL = 'sqlite:///modules.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Query all keywords
def check_keywords():
    print("Checking all keywords in the database...")
    keywords = session.query(Keyword).all()
    if not keywords:
        print("No keywords found in the database.")
    else:
        print(f"Found {len(keywords)} keywords:")
        for keyword in keywords:
            print(f"Keyword ID: {keyword.id}, Keyword: {keyword.keyword}")

# Query keywords for a specific module
def check_module_keywords(module_code):
    print(f"Checking keywords for module with code: {module_code}")
    module = session.query(Module).filter(Module.code == module_code).first()
    if module:
        print(f"Module: {module.name}")
        if module.keywords:
            print(f"Keywords for {module.name}:")
            for keyword in module.keywords:
                print(f"Keyword: {keyword.keyword}")
        else:
            print("No keywords associated with this module.")
    else:
        print(f"Module with code {module_code} not found.")

# Main execution
def main():
    check_keywords()
    # Replace 'M60034' with a valid module code for testing
    check_module_keywords('M60034')

if __name__ == "__main__":
    main()

# Close session
session.close()

