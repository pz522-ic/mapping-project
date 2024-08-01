from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from module_class import Base, Module, Keyword, module_keywords

# Database connection
DATABASE_URL = 'sqlite:///modules.db'
engine = create_engine(DATABASE_URL)
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()

def list_keywords():
    #all modules and their associated keywords
    modules = session.query(Module).all()
    
    for module in modules:
        print(f"Module: {module.code}")
        for keyword in module.keywords:
            print(f" - Keyword: {keyword.keyword}")

# Main function
def main():
    list_keywords()

if __name__ == "__main__":
    main()
