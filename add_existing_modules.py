def add_module(session, name, code, prerequisites, recommended_prerequisites, term, lecturer, assessments):
    # Convert list fields to strings
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

# Example 
add_module(
    session,
    name="Algebraic Topology",
    code="MATH60034/70034",
    prerequisites=["Linear Algebra and Groups", "Linear Algebra and Numerical Analysis", "Analysis II"],
    recommended_prerequisites="Groups and Rings",
    term="Spring",
    lecturer="Sara Veneziale",
    assessments=["Exam: 80%", "Coursework: 20%"]
)
