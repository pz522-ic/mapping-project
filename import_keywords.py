import sqlite3
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from module_class import Base, Module, Keyword, module_keywords

#  database connection for modules.db
DATABASE_URL = 'sqlite:///modules.db'
engine = create_engine(DATABASE_URL)
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()

#  connection for keywords.db
keywords_db = sqlite3.connect('keywords.db')
keywords_cursor = keywords_db.cursor()

def get_module_code_mapping():
    """
    Create a mapping from the old format (from keywords.db) to the new format (modules.db).
    """
    mapping = {
        'IUM':'MATH40001',
        'M40007':'MATH40007',
        'M50001_50017':'MATH5001_50017',
        'M50003_50016': 'MATH50003/50016', 
        'M50004_50015': 'MATH50004/50015',
        'M60001': 'MATH60001',
        
    }
    return mapping

def import_keywords():
    # Database setup for SQLite
    keywords_db_path = 'keywords.db'
    keywords_conn = sqlite3.connect(keywords_db_path)
    keywords_cursor = keywords_conn.cursor()

    module_code_mapping = get_module_code_mapping()

    # Iterate through all tables (modules) in the keywords database
    for table_name in keywords_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';"):
        table_name = table_name[0]
        print(f"Processing module with table: {table_name}")

        # Get the module code from the table name using the mapping
        module_code = table_name

        if module_code in module_code_mapping:
            module_code = module_code_mapping[module_code]

        # Find the module in the target database by code
        module = session.query(Module).filter(Module.code == module_code).first()

        if module:
            print(f"Found module with code: {module_code}")
            
            # Get keywords from the current table
            keywords_cursor.execute(f"SELECT * FROM {table_name};")
            rows = keywords_cursor.fetchall()

            for row in rows:
                _, _, keyword, _, _ = row
                keyword = keyword.strip()

                # Check if keyword already exists in the target database
                existing_keyword = session.query(Keyword).filter(Keyword.keyword == keyword).first()
                if not existing_keyword:
                    # Create new keyword if it doesn't exist
                    new_keyword = Keyword(keyword=keyword)
                    module.keywords.append(new_keyword)
                else:
                    module.keywords.append(existing_keyword)

            session.commit()
        else:
            print(f"Module with code {module_code} not found in the target database.")

    # Close connections
    keywords_conn.close()
    print("Import complete.")

# Main function
def main():
    import_keywords()

if __name__ == "__main__":
    main()