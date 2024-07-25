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



# Year 3 Applied Math
add_module(
    session,
    name="Fluid Dynamics 1",
    code="MATH60001/70001",
    prerequisites=["Calculus and Applications", "Multivariable Calculus and Differential Equations"],
    recommended_prerequisites="PDEs in Action",
    term="Autumn",
    lecturer="Xuesong Wu",
    assessments=["Exam: 80%", "Coursework: 20%"]
)


add_module(
    session,
    name="Fluid Dynamics 2",
    code="MATH60002/70002",
    prerequisites=["Calculus and Applications", "Multivariable Calculus and Differential Equations","Fluid Dynamics 1"],
    recommended_prerequisites="PDEs in Action",
    term="Spring",
    lecturer="Jonathan Mestel",
    assessments=["Exam: 80%", "Coursework: 20%"]
)


add_module(
    session,
    name="Introduction to Geophysical Fluid Dynamics",
    code="MATH60003/70003",
    prerequisites=["Calculus and Applications", "Multivariable Calculus and Differential Equations"],
    recommended_prerequisites="PDEs in Action",
    term="Spring",
    lecturer="Pavel Berloff",
    assessments=["Exam: 80%", "Coursework: 20%"]
)


add_module(
    session,
    name="Asymptotic Methods",
    code="MATH60004/70004",
    prerequisites=["Multivariable Calculus and Differential Equations"],
    recommended_prerequisites="None",
    term="Autumn",
    lecturer="Ory Schnitzer",
    assessments=["Exam: 80%", "Coursework: 20%"]
)


add_module(
    session,
    name="Optimisation",
    code="MATH60005/70005",
    prerequisites=["Calculus and Applications", "Multivariable Calculus and Differential Equations"],
    recommended_prerequisites="None",
    term="Autumn",
    lecturer="Dante Kalise, Karen Loayza-Romero",
    assessments=["Exam: 80%", "Coursework: 20%"]
)

add_module(
    session,
    name="Applied Complex Analysis",
    code="MATH60006/70006",
    prerequisites=["Analysis II"],
    recommended_prerequisites="None",
    term="Spring",
    lecturer="TBC",
    assessments=["Exam: 80%", "Coursework: 20%"]
)

add_module(
    session,
    name="Dynamics of Learning and Iterated Games",
    code="MATH60007/70007",
    prerequisites=["Calculus and Applications", "Multivariable Calculus and Differential Equations"],
    recommended_prerequisites="None",
    term="Autumn",
    lecturer="Sebastian van Strien",
    assessments=["Exam: 80%", "Coursework: 20%"]
)


add_module(
    session,
    name="Dynamical Systems",
    code="MATH60008/70008",
    prerequisites=["Calculus and Applications", "Multivariable Calculus and Differential Equations"],
    recommended_prerequisites="PDEs in Action",
    term="Autumn",
    lecturer="Jeroen Lamb",
    assessments=["Exam: 80%", "Coursework: 20%"]
)


add_module(
    session,
    name="Bifurcation Theory",
    code="MATH60009/70009",
    prerequisites=["Calculus and Applications", "Multivariable Calculus and Differential Equations"],
    recommended_prerequisites="None",
    term="Spring",
    lecturer="Dongchen Li",
    assessments=["Exam: 80%", "Coursework: 20%"]
)

add_module(
    session,
    name="Geometric Mechanics",
    code="MATH60010/70010",
    prerequisites=["Calculus and Applications", "Multivariable Calculus and Differential Equations"],
    recommended_prerequisites="PDEs in Action",
    term="Spring",
    lecturer="Darryl Holm",
    assessments=["Exam: 80%", "Coursework: 20%"]
)

add_module(
    session,
    name="Classical Dynamics",
    code="MATH60011/70011",
    prerequisites=["Calculus and Applications", "Multivariable Calculus and Differential Equations"],
    recommended_prerequisites="PDEs in Action",
    term="Autumn",
    lecturer="Oliver Street",
    assessments=["Exam: 80%", "Coursework: 20%"]
)

add_module(
    session,
    name="Mathematical Biology",
    code="MATH60014/70014",
    prerequisites=["Calculus and Applications", "Multivariable Calculus and Differential Equations"],
    recommended_prerequisites="PDEs in Action",
    term="Spring",
    lecturer="Paul Bressloff",
    assessments=["Exam: 80%", "Coursework: 20%"]
)

add_module(
    session,
    name="Quantum Mechanics 1",
    code="MATH60015/70015",
    prerequisites=["Calculus and Applications", "Multivariable Calculus and Differential Equations"],
    recommended_prerequisites="PDEs in Action",
    term="Autumn",
    lecturer="Eva-Marie Graefe",
    assessments=["Exam: 80%", "Coursework: 20%"]
)

