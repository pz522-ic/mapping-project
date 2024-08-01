from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from module_class import Module, Base  

# Connect to the SQLite database
engine = create_engine('sqlite:///modules.db')  
Session = sessionmaker(bind=engine)
session = Session()

def delete_module(session, name, code):
    # Query to find the module
    module_to_delete = session.query(Module).filter_by(name=name, code=code).first()
    
    if module_to_delete:
        session.delete(module_to_delete)
        session.commit()
        print(f"Module '{name}' with code '{code}' deleted successfully.")
    else:
        print(f"No module found with name '{name}' and code '{code}'.")

# Call the function to delete the module
delete_module(session, "Quantum Mechanics 2", "MATH60017/70017")

# Close the session
session.close()
