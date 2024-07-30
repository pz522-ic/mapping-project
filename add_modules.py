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
    name="Special Relativity and Electromagnetism",
    code="MATH60016/70016",
    prerequisites=["Calculus and Applications"],
    recommended_prerequisites="PDEs in Action",
    term="Autumn",
    lecturer="Gunnar Pruessner",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Quantum Mechanics 2",
    code="MATH60017/70017",
    prerequisites=["Calculus and Applications","Quantum Mechanics 1"],
    recommended_prerequisites=["PDEs in Action","Special Relativity and Electromagnetism"]
    term="Spring",
    lecturer="Ryan Barnett",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Special Relativity and Electromagnetism",
    code="MATH60018/70018",
    prerequisites=["Calculus and Applications"],
    recommended_prerequisites="None"
    term="Autumn",
    lecturer="Gunnar Pruessner",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Theory of Partial Differential Equations",
    code="MATH60019/70019",
    prerequisites=["Calculus and Applications","Multivariate Calculus and Differential Equations","PDEs in Action"],
    recommended_prerequisites="None",
    term="Autumn",
    lecturer="Massimo Sorella",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Function Spaces and Applications",
    code="MATH60020/70020",
    prerequisites=["Calculus and Applications","Multivariate Calculus and Differential Equations"],
    recommended_prerequisites="PDEs in Action",
    term="Autumn",
    lecturer="Pierre Germain",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Advanced Topics in Partial Differential Equations",
    code="MATH60021/70021",
    prerequisites=["Calculus and Applications","Multivariate Calculus and Differential Equations"],
    recommended_prerequisites="PDEs in Action",
    term="Spring",
    lecturer="Angeliki Menegaki",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Special Relativity and Electromagnetism",
    code="MATH60022/70022",
    prerequisites=["Calculus and Applications","Multivariate Calculus and Differential Equations"],
    recommended_prerequisites="PDEs in Action",
    term="Autumn",
    lecturer="Colin Cotter, David Ham",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Computational Dynamical Systems",
    code="MATH60023/70023",
    prerequisites=["Calculus and Applications","Multivariate Calculus and Differential Equations"],
    recommended_prerequisites="PDEs in Action",
    term="Autumn",
    lecturer="Eric Keaveny",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Computational Linear Algebra",
    code="MATH60024/70024",
    prerequisites=["Calculus and Applications","Linear  Algebrea and Numerical Analysis"],
    recommended_prerequisites="PDEs in Action",
    term="Autumn",
    lecturer="Colin Cotter",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Computational Partial Differential Equations",
    code="MATH60025/70025",
    prerequisites=["Calculus and Applications","PDEs in Action"],
    recommended_prerequisites="PDEs in Action",
    term="Spring",
    lecturer="Shahid Mughal",
    assessments=["Exam:90%, Coursework:10%"]
)
add_module(
    session,
    name="Methods for Data Science",
    code="MATH60026/70026",
    prerequisites=["Introduction to Computation"],
    recommended_prerequisites="Principles of Programming",
    term="Spring",
    lecturer="Barbara Bravi",
    assessments=["Exam:90%, Coursework:10%"]
)
add_module(
    session,
    name="Scientific Computation",
    code="MATH60027/70027",
    prerequisites=["Calculus and Applications","Linear  Algebrea and Numerical Analysis"],
    recommended_prerequisites="PDEs in Action",
    term="Autumn",
    lecturer="Prasun Ray",
    assessments=["Exam:90%, Coursework:10%"]
)
add_module(
    session,
    name="Mathematical Biology 2: Systems Biology",
    code="MATH60137/70137",
    prerequisites=["Calculus and Applications","Multivariate Calculus and Differential Equations"],
    recommended_prerequisites="PDEs in Action",
    term="Spring",
    lecturer="Omar Karin",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Introduction to Game Theory",
    code="MATH60141/70141",
    prerequisites=["Probability and Statistics","Calculus nad Applications"],
    recommended_prerequisites="None",
    term="Autumn",
    lecturer="Sam Brzezicki",
    assessments=["Exam:90%, Coursework:10%"]
)