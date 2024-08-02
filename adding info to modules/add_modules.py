from db_setup import session 
from module_class import Module  

def add_module(session, name, code, prerequisites, recommended_prerequisites, term, lecturer, assessments):
    # Convert lists to comma-separated strings
    prerequisites_str = ', '.join(prerequisites) if prerequisites else ""
    recommended_prerequisites_str = ', '.join(recommended_prerequisites) if isinstance(recommended_prerequisites, list) else recommended_prerequisites or ""
    assessments_str = ', '.join(assessments) if assessments else ""

    # Handle None values for fields that might be nullable
    recommended_prerequisites_str = recommended_prerequisites_str or ""
    summary_str = "" 
    learning_outcome_str = ""  
    
    new_module = Module(
        name=name,
        code=code,
        prerequisites=prerequisites_str,
        recommended_prerequisites=recommended_prerequisites_str,
        summary=summary_str,
        term=term,
        lecturer=lecturer,
        assessments=assessments_str,
        learning_outcome=learning_outcome_str
    )
    
    try:
        session.add(new_module)
        session.commit()
        print(f"Module '{name}' added successfully.")
    except Exception as e:
        session.rollback()
        print(f"Failed to add module '{name}': {e}")






#Example
add_module(
    session,
    name="Introduction to University Math",
    code="MATH40001",
    prerequisites=["None"],
    recommended_prerequisites="None",
    term="Autumn",
    lecturer="Marie Amalie Lawn, Eva-Marie Graefe, Charlotte Kestner",
    assessments=["Exam:90%, Coursework:10%"]
)



