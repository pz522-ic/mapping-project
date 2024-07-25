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

# Example Year 1
add_module(
    session,
    name="Analysis I",
    code="MATH40002",
    prerequisites=["None"],
    recommended_prerequisites="None",
    term="Autumn and Spring",
    lecturer="Ajay Chandra (Autumn), Marco Guaraco (Spring)",
    assessments=["Exam: 80%", "Coursework: 20%"]
)

add_module(
    session,
    name="Linear Algebra and Group Theory",
    code="MATH40003",
    prerequisites=["None"],
    recommended_prerequisites="None",
    term="Autumn and Spring",
    lecturer="Travis Schedler (Autumn), Michele Zordan (Spring)",
    assessments=["Exam: 80%", "Coursework: 20%"]
)

add_module(
    session,
    name="Calculus and Applications",
    code="MATH40004",
    prerequisites=["None"],
    recommended_prerequisites="None",
    term="Autumn and Spring",
    lecturer="Demetrios Papageorgiou (Autumn), Vahid Shahrezaei (Spring)",
    assessments=["Exam: 80%", "Coursework: 20%"]
)


add_module(
    session,
    name="Probability and Statistics",
    code="MATH40005",
    prerequisites=["None"],
    recommended_prerequisites="None",
    term="Autumn and Spring",
    lecturer="Ioanna Papatsouma (Autumn), Dean Bodenham (Spring)",
    assessments=["Exam: 80%", "Coursework: 20%"]
)

add_module(
    session,
    name="Introduction to Computation",
    code="MATH40006",
    prerequisites=["None"],
    recommended_prerequisites="None",
    term="Autumn and Spring",
    lecturer="Phil Ramsden",
    assessments=["Exam: 80%", "Coursework: 20%"]
)

add_module(
    session,
    name="An Introduction to Applied Maths",
    code="MATH40007",
    prerequisites=["None"],
    recommended_prerequisites="None",
    term="Spring",
    lecturer="Darren Crowdy",
    assessments=["Exam: 80%", "Coursework: 20%"]
)

add_module(
    session,
    name="M1R Research Project",
    code="MATH40008",
    prerequisites=["None"],
    recommended_prerequisites="None",
    term="Summer",
    lecturer="Michele Zordan (TBC)",
    assessments=["Exam: 80%", "Coursework: 20%"]
)


#Year 2
add_module(
    session,
    name="Analysis II",
    code="MATH50001/50017",
    prerequisites=["Analysis I"],
    recommended_prerequisites="None",
    term="Autumn and Spring",
    lecturer="Davoud Cheraghi,Nattalie Tamam",
    assessments=["Exam: 80%", "Coursework: 20%"]
)

add_module(
    session,
    name="Linear Algebra and Numerical Analysis",
    code="MATH50003/50012",
    prerequisites=["Linear Algebra and Group Theory"],
    recommended_prerequisites="None",
    term="Autumn and Spring",
    lecturer="Martin Liebeck,Sheehan Olver",
    assessments=["Exam: 80%", "Coursework: 20%"]
)

add_module(
    session,
    name="Multivariable Calculus and Differential Equations",
    code="MATH50004/50015",
    prerequisites=["None"],
    recommended_prerequisites="None",
    term="Autumn",
    lecturer="Andrew Walton, Martin Rasmussen",
    assessments=["Exam: 80%", "Coursework: 20%"]
)

add_module(
    session,
    name="Groups and Rings",
    code="MATH50005",
    prerequisites=["Linear Algebra and Group Theory"],
    recommended_prerequisites="None",
    term="Autumn",
    lecturer="Tom Coates",
    assessments=["Exam: 80%", "Coursework: 20%"]
)

add_module(
    session,
    name="Principles of Programming",
    code="MATH50009",
    prerequisites=["Introduction to Computation"],
    recommended_prerequisites="None",
    term="Autumn",
    lecturer="David Ham",
    assessments=["Exam: 80%", "Coursework: 20%"]
)

add_module(
    session,
    name="Lebesgue Measure and Integration",
    code="MATH50006",
    prerequisites=["Analysis I"],
    recommended_prerequisites="None",
    term="Spring",
    lecturer="Pierre-Francois Rodriguez",
    assessments=["Exam: 80%", "Coursework: 20%"]
)

add_module(
    session,
    name="Network Science",
    code="MATH50007",
    prerequisites=["None"],
    recommended_prerequisites="None",
    term="Spring",
    lecturer="Sarah Ferguson-Briggs",
    assessments=["Exam: 80%", "Coursework: 20%"]
)

add_module(
    session,
    name="Probability for Statistics",
    code="MATH50010",
    prerequisites=["Probability and Statistics"],
    recommended_prerequisites="None",
    term="Autumn",
    lecturer="Ciara Pike-Burke",
    assessments=["Exam: 80%", "Coursework: 20%"]
)

add_module(
    session,
    name="Statistical Modelling 1",
    code="MATH50011",
    prerequisites=["Probability and Statistics"],
    recommended_prerequisites="Probability for Statistics",
    term="Spring",
    lecturer="Riccardo Passeggeri",
    assessments=["Exam: 80%", "Coursework: 20%"]
)

add_module(
    session,
    name="PDEs in Action",
    code="MATH50008",
    prerequisites=["Probability and Statistics"],
    recommended_prerequisites="Calculus and Applications",
    term="Spring",
    lecturer="Thibault Bertrand",
    assessments=["Exam: 80%", "Coursework: 20%"]
)


# Year 3
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


