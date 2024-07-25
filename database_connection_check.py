from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Database setup
DATABASE_URL = 'sqlite:///modules.db'  # This assumes modules.db is in the same directory as main.py
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def check_connection():
    try:
        # Use SQLAlchemy's text function to execute raw SQL
        result = session.execute(text('SELECT 1'))
        print("Database connection is successful.")
    except Exception as e:
        print(f"Error connecting to the database: {e}")

check_connection()

from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

# Database setup
DATABASE_URL = 'sqlite:///modules.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def check_schema():
    try:
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        print(f"Tables: {tables}")
        
        for table in tables:
            columns = inspector.get_columns(table)
            print(f"Table: {table}")
            for column in columns:
                print(f"Column: {column['name']} - Type: {column['type']}")
    except Exception as e:
        print(f"Error checking schema: {e}")

check_schema()
