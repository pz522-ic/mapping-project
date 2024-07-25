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
