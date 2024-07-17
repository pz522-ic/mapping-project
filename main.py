import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# Updated database of modules
modules_db = {
    "Introduction to University Math (MATH40001/40009)": {
        "prerequisites": [],
        "summary": "Introduction to university mathematics.",
        "term": "Autumn",
        "lecturer": "Marie Amalie Lawn, Eva-Marie Graefe, Charlotte Kestner",
        "assessments": ["Exam", "Coursework"],
        "type": "Compulsory"
    },
    "Analysis I (MATH40002)": {
        "prerequisites": [],
        "summary": "Introduction to analysis.",
        "term": "Autumn and Spring",
        "lecturer": "Ajay Chandra (T1), Marco Guaraco (T2)",
        "assessments": ["Exam", "Coursework"],
        "type": "Compulsory"
    },
    "Linear Algebra and Group Theory (MATH40003)": {
        "prerequisites": [],
        "summary": "Introduction to linear algebra and group theory.",
        "term": "Autumn and Spring",
        "lecturer": "Travis Schedler (T1), Michele Zordan (T2)",
        "assessments": ["Exam", "Coursework"],
        "type": "Compulsory"
    },
    "Calculus and Applications (MATH40004)": {
        "prerequisites": [],
        "summary": "Introduction to calculus and its applications.",
        "term": "Autumn and Spring",
        "lecturer": "Demetrios Papageorgiou (T1), Vahid Shahrezaei (T2)",
        "assessments": ["Exam", "Coursework"],
        "type": "Compulsory"
    },
    "Probability and Statistics (MATH40005)": {
        "prerequisites": [],
        "summary": "Introduction to probability and statistics.",
        "term": "Autumn and Spring",
        "lecturer": "Ioanna Papatsouma (T1), Dean Bodenham (T2)",
        "assessments": ["Exam", "Coursework"],
        "type": "Compulsory"
    },
    "Introduction to Computation (MATH40006)": {
        "prerequisites": [],
        "summary": "Introduction to computation.",
        "term": "Autumn",
        "lecturer": "Phil Ramsden",
        "assessments": ["Exam", "Coursework"],
        "type": "Compulsory"
    },
    "An Introduction to Applied Maths (MATH40007)": {
        "prerequisites": [],
        "summary": "Introduction to applied mathematics.",
        "term": "Autumn",
        "lecturer": "Darren Crowdy",
        "assessments": ["Exam", "Coursework"],
        "type": "Compulsory"
    },
    "M1R (MATH40008)": {
        "prerequisites": [],
        "summary": "Mathematics 1 Revision.",
        "term": "To be confirmed",
        "lecturer": "Michele Zordan",
        "assessments": ["Exam", "Coursework"],
        "type": "Compulsory"
    },
    "Linear Algebra (JMC) (MATH40012)": {
        "prerequisites": [],
        "summary": "Linear Algebra for JMC students.",
        "term": "Autumn and Spring",
        "lecturer": "Benjamin Briggs (T1) Alexei Skorobogatov (T2)",
        "assessments": ["Exam", "Coursework"],
        "type": "Compulsory"
    },
    "Analysis 2: Real Analysis and Topology (MATH50001/50017)": {
        "prerequisites": ["Analysis I"],
        "summary": "Advanced real analysis and topology.",
        "term": "Autumn",
        "lecturer": "Davoud Cheraghi (T1)",
        "assessments": ["Exam", "Coursework"],
        "type": "Compulsory"
    },
    "Analysis 2: Complex Analysis (MATH50001/50018)": {
        "prerequisites": ["Analysis I"],
        "summary": "Complex analysis.",
        "term": "Spring",
        "lecturer": "Nattalie Tamam (T2)",
        "assessments": ["Exam", "Coursework"],
        "type": "Compulsory"
    },
    "M2R (MATH50002/MATH50014)": {
        "prerequisites": [],
        "summary": "Mathematics 2 Revision.",
        "term": "Autumn and Spring",
        "lecturer": "Thibault Bertrand",
        "assessments": ["Exam", "Coursework"],
        "type": "Compulsory"
    },
    "Linear Algebra (MATH50003/50012)": {
        "prerequisites": ["Linear Algebra and Group Theory"],
        "summary": "Advanced linear algebra.",
        "term": "Autumn",
        "lecturer": "Martin Liebeck (T1)",
        "assessments": ["Exam", "Coursework"],
        "type": "Compulsory"
    },
    "Numerical Analysis (MATH50003/50016)": {
        "prerequisites": ["Linear Algebra and Group Theory"],
        "summary": "Numerical methods for solving mathematical problems.",
        "term": "Spring",
        "lecturer": "Sheehan Olver (T2)",
        "assessments": ["Exam", "Coursework"],
        "type": "Compulsory"
    },
    "Multivariable Calculus (MATH50004/50015)": {
        "prerequisites": ["Calculus and Applications"],
        "summary": "Multivariable calculus.",
        "term": "Autumn",
        "lecturer": "Andrew Walton (T1)",
        "assessments": ["Exam", "Coursework"],
        "type": "Compulsory"
    },
    "Differential Equations (MATH50004/50019)": {
        "prerequisites": ["Calculus and Applications"],
        "summary": "Introduction to differential equations.",
        "term": "Spring",
        "lecturer": "Martin Rasmussen (T2)",
        "assessments": ["Exam", "Coursework"],
        "type": "Compulsory"
    },
    "Groups and Rings (MATH50005)": {
        "prerequisites": ["Linear Algebra and Group Theory"],
        "summary": "Study of groups and rings.",
        "term": "Autumn",
        "lecturer": "Tom Coates (T1)",
        "assessments": ["Exam", "Coursework"],
        "type": "Compulsory"
    },
    "Lebesgue Measure and Integration (MATH50006)": {
        "prerequisites": ["Analysis I"],
        "summary": "Lebesgue measure theory and integration.",
        "term": "Spring",
        "lecturer": "Pierre-Francois Rodriguez (T2)",
        "assessments": ["Exam", "Coursework"],
        "type": "Compulsory"
    },
    "Network Science (MATH50007)": {
        "prerequisites": [],
        "summary": "Introduction to network science.",
        "term": "Spring",
        "lecturer": "Sarah Ferguson-Briggs (T2)",
        "assessments": ["Exam", "Coursework"],
        "type": "Compulsory"
    },
    "PDEs in Action (MATH50008)": {
        "prerequisites": [],
        "summary": "Partial differential equations in action.",
        "term": "Spring",
        "lecturer": "Thibault Bertrand (T2)",
        "assessments": ["Exam", "Coursework"],
        "type": "Compulsory"
    },
    "Principles of Programming (MATH50009)": {
        "prerequisites": [],
        "summary": "Principles of programming.",
        "term": "Autumn",
        "lecturer": "David Ham (T1)",
        "assessments": ["Exam", "Coursework"],
        "type": "Compulsory"
    },
    "Probability for Statistics (MATH50010)": {
        "prerequisites": [],
        "summary": "Probability theory for statistics.",
        "term": "Autumn",
        "lecturer": "Ciara Pike-Burke (T1)",
        "assessments": ["Exam", "Coursework"],
        "type": "Compulsory"
    },
    "Statistical Modelling 1 (MATH50011)": {
        "prerequisites": [],
        "summary": "Introduction to statistical modelling.",
        "term": "Spring",
        "lecturer": "Riccardo Passeggeri (T2)",
        "assessments": ["Exam", "Coursework"],
        "type": "Compulsory"
    },
    "Probability (JMC) (MATH50013)": {
        "prerequisites": [],
        "summary": "Probability for JMC students.",
        "term": "Autumn",
        "lecturer": "Tomasz Kosmala (T1)",
        "assessments": ["Exam", "Coursework"],
        "type": "Compulsory"
    },
    "Machine Learning (MATH60001)": {
        "prerequisites": ["Multivariable Calculus", "Linear Algebra and Group Theory"],
        "summary": "Introduction to machine learning.",
        "term": "Autumn",
        "lecturer": "Irene Davis",
        "assessments": ["Exam", "Coursework"],
        "type": "Optional"
    },
    "Galois Theory (MATH60002)": {
        "prerequisites": ["Groups and Rings"],
        "summary": "Advanced Galois theory.",
        "term": "Spring",
        "lecturer": "Jack Clark",
        "assessments": ["Exam", "Coursework"],
        "type": "Optional"
    },
    "Fluid Dynamics I (MATH60003)": {
        "prerequisites": ["Differential Equations"],
        "summary": "Introduction to fluid dynamics.",
        "term": "Autumn",
        "lecturer": "Karen Martinez",
        "assessments": ["Exam", "Coursework"],
        "type": "Optional"
    }
}

# Organize modules by year
modules_by_year = {
    "Year 1": [
        "Introduction to University Math (MATH40001/40009)",
        "Analysis I (MATH40002)",
        "Linear Algebra and Group Theory (MATH40003)",
        "Calculus and Applications (MATH40004)",
        "Probability and Statistics (MATH40005)",
        "Introduction to Computation (MATH40006)",
        "An Introduction to Applied Maths (MATH40007)",
        "M1R (MATH40008)",
        "Linear Algebra (JMC) (MATH40012)"
    ],
    "Year 2": [
        "Analysis 2: Real Analysis and Topology (MATH50001/50017)",
        "Analysis 2: Complex Analysis (MATH50001/50018)",
        "M2R (MATH50002/MATH50014)",
        "Linear Algebra (MATH50003/50012)",
        "Numerical Analysis (MATH50003/50016)",
        "Multivariable Calculus (MATH50004/50015)",
        "Differential Equations (MATH50004/50019)",
        "Groups and Rings (MATH50005)",
        "Lebesgue Measure and Integration (MATH50006)",
        "Network Science (MATH50007)",
        "PDEs in Action (MATH50008)",
        "Principles of Programming (MATH50009)",
        "Probability for Statistics (MATH50010)",
        "Statistical Modelling 1 (MATH50011)",
        "Probability (JMC) (MATH50013)"
    ],
    "Year 3": [
        "Machine Learning (MATH60001)",
        "Galois Theory (MATH60002)",
        "Fluid Dynamics I (MATH60003)"
    ]
}

degrees_info = {
    "G100": {
        "Year 2": {
            "Group A": ["Analysis 2: Real Analysis and Topology (MATH50001/50017)", "Groups and Rings (MATH50005)"],
            "Group B": ["Analysis 2: Complex Analysis (MATH50001/50018)", "M2R (MATH50002/MATH50014)", "Linear Algebra (MATH50003/50012)", "Numerical Analysis (MATH50003/50016)", "Multivariable Calculus (MATH50004/50015)", "Differential Equations (MATH50004/50019)", "Lebesgue Measure and Integration (MATH50006)", "Network Science (MATH50007)", "PDEs in Action (MATH50008)", "Principles of Programming (MATH50009)", "Probability for Statistics (MATH50010)", "Statistical Modelling 1 (MATH50011)"]
        }
    },
    "G102": {
        "Year 2": {
            "Group A": ["Analysis 2: Real Analysis and Topology (MATH50001/50017)", "Groups and Rings (MATH50005)"],
            "Group B": ["Analysis 2: Complex Analysis (MATH50001/50018)", "M2R (MATH50002/MATH50014)", "Linear Algebra (MATH50003/50012)", "Numerical Analysis (MATH50003/50016)", "Multivariable Calculus (MATH50004/50015)", "Differential Equations (MATH50004/50019)", "Lebesgue Measure and Integration (MATH50006)", "Network Science (MATH50007)", "PDEs in Action (MATH50008)", "Principles of Programming (MATH50009)", "Probability for Statistics (MATH50010)", "Statistical Modelling 1 (MATH50011)"],
            "Core": ["Network Science (MATH50007)", "Principles of Programming (MATH50009)"]
        }
    },
    "G125": {
        "Year 2": {
            "Group A": ["Analysis 2: Real Analysis and Topology (MATH50001/50017)", "Groups and Rings (MATH50005)"],
            "Group B": ["Analysis 2: Complex Analysis (MATH50001/50018)", "M2R (MATH50002/MATH50014)", "Linear Algebra (MATH50003/50012)", "Numerical Analysis (MATH50003/50016)", "Multivariable Calculus (MATH50004/50015)", "Differential Equations (MATH50004/50019)", "Lebesgue Measure and Integration (MATH50006)", "Network Science (MATH50007)", "PDEs in Action (MATH50008)", "Principles of Programming (MATH50009)", "Probability for Statistics (MATH50010)", "Statistical Modelling 1 (MATH50011)"],
            "Core": ["Groups and Rings (MATH50005)", "Lebesgue Measure and Integration (MATH50006)"]
        }
    },
    "G1F3": {
        "Year 2": {
            "Group A": ["Analysis 2: Real Analysis and Topology (MATH50001/50017)", "Groups and Rings (MATH50005)"],
            "Group B": ["Analysis 2: Complex Analysis (MATH50001/50018)", "M2R (MATH50002/MATH50014)", "Linear Algebra (MATH50003/50012)", "Numerical Analysis (MATH50003/50016)", "Multivariable Calculus (MATH50004/50015)", "Differential Equations (MATH50004/50019)", "Lebesgue Measure and Integration (MATH50006)", "Network Science (MATH50007)", "PDEs in Action (MATH50008)", "Principles of Programming (MATH50009)", "Probability for Statistics (MATH50010)", "Statistical Modelling 1 (MATH50011)"],
            "Core": ["PDEs in Action (MATH50008)"]
        }
    },
    "G1G3": {
        "Year 2": {
            "Group A": ["Analysis 2: Real Analysis and Topology (MATH50001/50017)", "Groups and Rings (MATH50005)"],
            "Group B": ["Analysis 2: Complex Analysis (MATH50001/50018)", "M2R (MATH50002/MATH50014)", "Linear Algebra (MATH50003/50012)", "Numerical Analysis (MATH50003/50016)", "Multivariable Calculus (MATH50004/50015)", "Differential Equations (MATH50004/50019)", "Lebesgue Measure and Integration (MATH50006)", "Network Science (MATH50007)", "PDEs in Action (MATH50008)", "Principles of Programming (MATH50009)", "Probability for Statistics (MATH50010)", "Statistical Modelling 1 (MATH50011)"],
            "Core": ["Probability for Statistics (MATH50010)", "Statistical Modelling 1 (MATH50011)"]
        }
    },
    "G1GH": {
        "Year 2": {
            "Group A": ["Analysis 2: Real Analysis and Topology (MATH50001/50017)", "Groups and Rings (MATH50005)"],
            "Group B": ["Analysis 2: Complex Analysis (MATH50001/50018)", "M2R (MATH50002/MATH50014)", "Linear Algebra (MATH50003/50012)", "Numerical Analysis (MATH50003/50016)", "Multivariable Calculus (MATH50004/50015)", "Differential Equations (MATH50004/50019)", "Lebesgue Measure and Integration (MATH50006)", "Network Science (MATH50007)", "PDEs in Action (MATH50008)", "Principles of Programming (MATH50009)", "Probability for Statistics (MATH50010)", "Statistical Modelling 1 (MATH50011)"],
            "Core": ["Probability for Statistics (MATH50010)", "Statistical Modelling 1 (MATH50011)"]
        }
    },
    "GG31": {
        "Year 2": {
            "Group A": ["Analysis 2: Real Analysis and Topology (MATH50001/50017)", "Groups and Rings (MATH50005)"],
            "Group B": ["Analysis 2: Complex Analysis (MATH50001/50018)", "M2R (MATH50002/MATH50014)", "Linear Algebra (MATH50003/50012)", "Numerical Analysis (MATH50003/50016)", "Multivariable Calculus (MATH50004/50015)", "Differential Equations (MATH50004/50019)", "Lebesgue Measure and Integration (MATH50006)", "Network Science (MATH50007)", "PDEs in Action (MATH50008)", "Principles of Programming (MATH50009)", "Probability for Statistics (MATH50010)", "Statistical Modelling 1 (MATH50011)"],
            "Core": ["Probability for Statistics (MATH50010)", "Statistical Modelling 1 (MATH50011)"]
        }
    },
    "G103": {
        "Year 2": {
            "Group A": ["Analysis 2: Real Analysis and Topology (MATH50001/50017)", "Groups and Rings (MATH50005)"],
            "Group B": ["Analysis 2: Complex Analysis (MATH50001/50018)", "M2R (MATH50002/MATH50014)", "Linear Algebra (MATH50003/50012)", "Numerical Analysis (MATH50003/50016)", "Multivariable Calculus (MATH50004/50015)", "Differential Equations (MATH50004/50019)", "Lebesgue Measure and Integration (MATH50006)", "Network Science (MATH50007)", "PDEs in Action (MATH50008)", "Principles of Programming (MATH50009)", "Probability for Statistics (MATH50010)", "Statistical Modelling 1 (MATH50011)"]
        }
    },
    "G104": {
        "Year 2": {
            "Group A": ["Analysis 2: Real Analysis and Topology (MATH50001/50017)", "Groups and Rings (MATH50005)"],
            "Group B": ["Analysis 2: Complex Analysis (MATH50001/50018)", "M2R (MATH50002/MATH50014)", "Linear Algebra (MATH50003/50012)", "Numerical Analysis (MATH50003/50016)", "Multivariable Calculus (MATH50004/50015)", "Differential Equations (MATH50004/50019)", "Lebesgue Measure and Integration (MATH50006)", "Network Science (MATH50007)", "PDEs in Action (MATH50008)", "Principles of Programming (MATH50009)", "Probability for Statistics (MATH50010)", "Statistical Modelling 1 (MATH50011)"]
        }
    }
}

# Sidebar navigation
st.sidebar.title("Navigation")
tabs = ["Home", "Module Information", "Degree Information"]
selection = st.sidebar.radio("Go to", tabs)

if selection == "Home":
    st.title("Welcome to the Maths Department Module Information System")
    st.write("""
        This is a platform where you can find detailed information about the modules offered in our Mathematics Department. 
        Use the sidebar to navigate through the different sections.
    """)
elif selection == "Module Information":
    st.title("Module Information")
    year = st.selectbox("Select Year", list(modules_by_year.keys()))
    selected_module = st.selectbox("Select Module", modules_by_year[year])
    
    module_info = modules_db[selected_module]
    st.header(selected_module)
    st.write(f"**Prerequisites**: {', '.join(module_info['prerequisites']) if module_info['prerequisites'] else 'None'}")
    st.write(f"**Summary**: {module_info['summary']}")
    st.write(f"**Term**: {module_info['term']}")
    st.write(f"**Lecturer**: {module_info['lecturer']}")
    st.write(f"**Assessments**: {', '.join(module_info['assessments'])}")
    st.write(f"**Type**: {module_info['type']}")

elif selection == "Degree Information":
    st.title("Degree Information")
    degree = st.selectbox("Select Degree", list(degrees_info.keys()))
    year = st.selectbox("Select Year", ["Year 1", "Year 2", "Year 3", "Year 4"])
    
    if year in degrees_info[degree]:
        st.subheader(f"Degree: {degree} - {year}")
        group_a_modules = degrees_info[degree][year].get("Group A", [])
        group_b_modules = degrees_info[degree][year].get("Group B", [])
        core_modules = degrees_info[degree][year].get("Core", [])
        
        st.write("### Group A Modules")
        for module in group_a_modules:
            st.write(f"- {module}")
        
        st.write("### Group B Modules")
        for module in group_b_modules:
            st.write(f"- {module}")
        
        if core_modules:
            st.write("### Core Modules")
            for module in core_modules:
                st.write(f"- {module}")
    else:
        st.write("No information available for the selected year and degree.")
