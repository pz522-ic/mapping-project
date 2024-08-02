from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from module_class import Base, Module  

# database connection
DATABASE_URL = "sqlite:///modules.db"  
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def update_module(name, new_code=None, new_prerequisites=None, new_recommended_prerequisites=None,
                   new_term=None, new_lecturer=None, new_assessments=None, new_summary=None, new_learning_outcome=None):
    try:
        # module by name
        module = session.query(Module).filter_by(name=name).first()
        
        if not module:
            print(f"Module '{name}' not found.")
            return
        
        # Update module fields if new values are provided
        if new_code is not None:
            module.code = new_code
        if new_prerequisites is not None:
            module.prerequisites = ', '.join(new_prerequisites) if isinstance(new_prerequisites, list) else new_prerequisites
        if new_recommended_prerequisites is not None:
            module.recommended_prerequisites = ', '.join(new_recommended_prerequisites) if isinstance(new_recommended_prerequisites, list) else new_recommended_prerequisites
        if new_term is not None:
            module.term = new_term
        if new_lecturer is not None:
            module.lecturer = new_lecturer
        if new_assessments is not None:
            module.assessments = ', '.join(new_assessments) if isinstance(new_assessments, list) else new_assessments
        if new_summary is not None:
            module.summary = new_summary
        if new_learning_outcome is not None:
            module.learning_outcome = new_learning_outcome
        
        # Commit the changes 
        session.commit()
        print(f"Module '{name}' updated successfully.")
    
    except Exception as e:
        session.rollback()
        print(f"Failed to update module '{name}': {e}")

# Example usage
if __name__ == "__main__":
    update_module(
        name="Quantum Mechanics 2",
        new_code="MATH60017/70017",
        new_prerequisites=["Calculus and Applications", "Quantum Mechanics 1"],
        new_recommended_prerequisites=["PDEs in Action", "Special Relativity and Electromagnetism"],
        new_term="Spring",
        new_lecturer="Ryan Barnett",
        new_assessments=["Exam:80%, Coursework:20%"],  # Example updated assessments
        new_summary="An advanced study of quantum mechanics.",
        new_learning_outcome="Students will understand advanced quantum theories."
    )




