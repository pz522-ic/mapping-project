import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from module_class import Base, Module, Keyword, module_keywords

# Database connection for modules.db
DATABASE_URL = 'sqlite:///modules.db'
engine = create_engine(DATABASE_URL)
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()

# Connection for keywords.db
keywords_db = sqlite3.connect('keywords.db')
keywords_cursor = keywords_db.cursor()

def get_module_code_mapping():
    """
    Create a mapping from the old format (from keywords.db) to the new format (modules.db).
    """
    mapping = {
        'IUM': 'MATH40001',
        'M40005':'MATH40005',
        'M40006':'MATH40006',
        'M40007':'MATH40007',
        'M40008':'MATH40008',
        'M50009': 'MATH50009',
        'M50011': 'MATH50011',
        'M50001_50017': 'MATH50001/50017',
        'M50001_50018': 'MATH50001/50017',
        'M50003_50012': 'MATH50003/50012',
        'M50003_50016': 'MATH50003/50012',
        'M50004_50015': 'MATH50004/50015',
        'M50004_50019': 'MATH50004/50015',
        # Add more mappings as needed
    }
    return mapping

def import_keywords():
    # Get the module code mapping
    module_code_mapping = get_module_code_mapping()

    # Iterate through all tables (modules) in the keywords database
    keywords_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = keywords_cursor.fetchall()

    for table_name_tuple in tables:
        table_name = table_name_tuple[0]
        print(f"Processing module with table: {table_name}")

        # Get the module code from the table name using the mapping
        module_code = module_code_mapping.get(table_name, table_name)

        # Find the module in the target database by code
        module = session.query(Module).filter(Module.code == module_code).first()

        if module:
            print(f"Found module with code: {module_code}")

            # Get keywords from the current table
            keywords_cursor.execute(f"SELECT * FROM {table_name};")
            rows = keywords_cursor.fetchall()

            for row in rows:
                keyword = row[2].strip()  # Assuming the keyword is in the third column

                # Check if keyword already exists in the target database
                existing_keyword = session.query(Keyword).filter(Keyword.keyword == keyword).first()
                if not existing_keyword:
                    # Create new keyword if it doesn't exist
                    new_keyword = Keyword(keyword=keyword)
                    session.add(new_keyword)
                    session.commit()  # Commit here to ensure new keyword is saved and has an ID
                    module.keywords.append(new_keyword)
                else:
                    # Append the existing keyword
                    if existing_keyword not in module.keywords:
                        module.keywords.append(existing_keyword)

            # Commit the session after processing all keywords for the module
            session.commit()
        else:
            print(f"Module with code {module_code} not found in the target database.")

    # Close connections
    keywords_db.close()
    print("Import complete.")

# Main function
def main():
    import_keywords()

if __name__ == "__main__":
    main()


