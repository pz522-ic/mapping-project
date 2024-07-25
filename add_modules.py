from db_setup import session 
from module_class import Module  

def add_module(session, name, code, prerequisites, recommended_prerequisites, term, lecturer, assessments):
    prerequisites_str = ', '.join(prerequisites) if prerequisites else ""
    assessments_str = ', '.join(assessments) if assessments else ""
    
    new_module = Module(
        name=name,
        code=code,
        prerequisites=prerequisites_str,
        recommended_prerequisites=recommended_prerequisites,
        term=term,
        lecturer=lecturer,
        assessments=assessments_str
    )
    
    session.add(new_module)
    session.commit()
    print(f"Module '{name}' added successfully.")



# Year 3 

add_module(
    session,
    name="M1R Research Project",
    code="MATH40008",
    prerequisites=["None"],
    recommended_prerequisites="None",
    term="Summer",
    lecturer="Michele Zordan",
    assessments=["Paper:80% Presentation:20%"]
)