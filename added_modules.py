
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
## Applied Math
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


add_module(
    session,
    name="Quantum Mechanics 2",
    code="MATH60017/70017",
    prerequisites=["Calculus and Applications","Quantum Mechanics 1"],
    recommended_prerequisites=["PDEs in Action","Special Relativity and Electromagnetism"],
    term="Spring",
    lecturer="Ryan Barnett",
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

# Year 3 
##Math finance
add_module(
    session,
    name="Mathematical Finance: An Introduction to Option Pricing",
    code="MATH60012/70012",
    prerequisites=["Probability and Statistics","Calculus nad Applications"],
    recommended_prerequisites="None",
    term="Autumn",
    lecturer="Pietro Siorpaes",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Stochastic Differential Equations in Financial Modelling",
    code="MATH60130/70130",
    prerequisites=["Probability and Statistics","Calculus and Applications"],
    recommended_prerequisites="None",
    term="Autumn",
    lecturer="Damiano Brigo",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Rough Paths and Applications to Machine Learning",
    code="MATH60138/70138",
    prerequisites=["Probability and Statistics","Calculus nad Applications"],
    recommended_prerequisites="Methods for Data Science",
    term="Spring",
    lecturer="Chris Salvi",
    assessments=["Exam:90%, Coursework:10%"]
)
    
# Year 3 
##Pure Maths
add_module(
    session,
    name="Probability Theory",
    code="MATH60028/70028",
    prerequisites=["Probability and Statistics"],
    recommended_prerequisites="Lebesgue Measure and Integration",
    term="Autumn",
    lecturer="Ajay Chandra",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Functional Analysis",
    code="MATH60029/70029",
    prerequisites=["Probability and Statistics","Analysis I"],
    recommended_prerequisites="Lebesgue Measure and Integration",
    term="Spring",
    lecturer="Pierre-Francois Rodriguez",
    assessments=["Exam:90%, Coursework:10%"]
)


add_module(
    session,
    name="Fourier Analysis and the Theory of Distributions",
    code="MATH60030/70030",
    prerequisites=["Calculus and Applications"],
    recommended_prerequisites="None",
    term="Spring",
    lecturer="Igor Krasovsky",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Markov Processes",
    code="MATH60031/70031",
    prerequisites=["Probability and Statistics","Probability for Statistics"],
    recommended_prerequisites="None",
    term="Autumn",
    lecturer="Zhiyuan Zhang",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Geometry of Curves and Surfaces",
    code="MATH60032/70032",
    prerequisites=["Calculus and Applications"],
    recommended_prerequisites="None",
    term="Spring",
    lecturer="Steven Sivek",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Algebraic Curves",
    code="MATH60033/70033",
    prerequisites=["Calculus and Applications","Multivariate Calculus and Differential Equations"],
    recommended_prerequisites="None",
    term="Autumn",
    lecturer="Soheyla Feyzbakhsh",
    assessments=["Exam:90%, Coursework:10%"]
)


add_module(
    session,
    name="Algebraic Topology",
    code="MATH60034/70034",
    prerequisites=["Calculus nad Applications","Multivariate Calculus and Differential Equations"],
    recommended_prerequisites="None",
    term="Spring",
    lecturer="Sara Veneziale",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Algebra 3",
    code="MATH60035/70035",
    prerequisites=["Groups and Rings"],
    recommended_prerequisites="None",
    term="Autumn",
    lecturer="Alessio Corti",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Group Theory",
    code="MATH60036/70036",
    prerequisites=["Groups and Rings"],
    recommended_prerequisites="None",
    term="Autumn",
    lecturer="Martin Liebeck",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Galois Theory",
    code="MATH60037/70037",
    prerequisites=["Groups and Rings"],
    recommended_prerequisites="None",
    term="Autumn",
    lecturer="Alexei Skorobogatov",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Graph Theory",
    code="MATH60038/70038",
    prerequisites=["Groups and Rings"],
    recommended_prerequisites="None",
    term="Autumn",
    lecturer="Michele Zordan",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Group Representation Theory",
    code="MATH60039/70039",
    prerequisites=["Groups and Rings"],
    recommended_prerequisites="None",
    term="Spring",
    lecturer="Heather MacBeth",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Formalising Mathematics",
    code="MATH60040/70040",
    prerequisites="None",
    recommended_prerequisites="None",
    term="Spring",
    lecturer="Bhavik Mehta",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Number Theory",
    code="MATH60041/70041",
    prerequisites="None",
    recommended_prerequisites="None",
    term="Autumn",
    lecturer="Ambrus Pal",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Algebraic Number Theory",
    code="MATH60042/70042",
    prerequisites="None",
    recommended_prerequisites="None",
    term="Spring",
    lecturer="Margherita Pagano",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Mathematical Logic",
    code="MATH60132/70132",
    prerequisites="None",
    recommended_prerequisites="None",
    term="Spring",
    lecturer="David Evans",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Geometric Complex Analysis",
    code="MATH60140/70140",
    prerequisites=["Analysis II"],
    recommended_prerequisites="None",
    term="Spring",
    lecturer="Davoud Cheraghi",
    assessments=["Exam:90%, Coursework:10%"]
)


#Year 3
##Statistics

add_module(
    session,
    name="Statistical Theory",
    code="MATH60043/70043",
    prerequisites=["Probability and Statistics"],
    recommended_prerequisites="None",
    term="Spring",
    lecturer="Kolyan Ray",
    assessments=["Exam:90%, Coursework:10%"]
)



add_module(
    session,
    name="Applied Statistical Inference",
    code="MATH60044/70044",
    prerequisites=["Probability and Statistics"],
    recommended_prerequisites="None",
    term="Autumn",
    lecturer="Chris Hallsworth",
    assessments=["Exam:90%, Coursework:10%"]
)


add_module(
    session,
    name="Applied Probability",
    code="MATH60045/70045",
    prerequisites=["Probability and Statistics"],
    recommended_prerequisites="None",
    term="Autumn",
    lecturer="Robin Ryder",
    assessments=["Exam:90%, Coursework:10%"]
)


add_module(
    session,
    name="Time Series Analysis",
    code="MATH60046/70046",
    prerequisites=["Probability and Statistics"],
    recommended_prerequisites="None",
    term="Spring",
    lecturer="Ed Cohen",
    assessments=["Exam:90%, Coursework:10%"]
)


add_module(
    session,
    name="Stochastic Simulation",
    code="MATH60047/70047",
    prerequisites=["Probability and Statistics"],
    recommended_prerequisites="None",
    term="Autumn",
    lecturer="Deniz Akyildiz",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Survival Models",
    code="MATH60048/70048",
    prerequisites=["Probability and Statistics"],
    recommended_prerequisites="None",
    term="Autumn",
    lecturer="Heather Battey",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Introduction to Statistical Learning",
    code="MATH60049/70049",
    prerequisites=["Probability and Statistics"],
    recommended_prerequisites="None",
    term="Spring",
    lecturer="Guy Nason",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Spatial Statistics",
    code="MATH60139/70139",
    prerequisites=["Probability and Statistics"],
    recommended_prerequisites="None",
    term="Spring",
    lecturer="Adam Sykulski",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="Mathematics of Business and Economics",
    code="MATH60142/70142",
    prerequisites=["Probability and Statistics"],
    recommended_prerequisites="None",
    term="Spring",
    lecturer="Max Autenrieth",
    assessments=["Exam:90%, Coursework:10%"]
)

add_module(
    session,
    name="M3R",
    code="MATH60050",
    prerequisites=["Probability and Statistics"],
    recommended_prerequisites="None",
    term="Spring",
    lecturer="None",
    assessments=["Paper:90%, presentation:10%"]
)

