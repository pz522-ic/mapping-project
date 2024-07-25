
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

add_module(
    session,
    name="M2R Research Project",
    code="MATH50002/50014",
    prerequisites=["None"],
    recommended_prerequisites="None",
    term="Summer",
    lecturer="Thibault Bertrand",
    assessments=["Poster:80% Presentation:20%"]
)


