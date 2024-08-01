import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from module_class import Module, Keyword

# Database setup
engine = create_engine('sqlite:///modules.db')
Session = sessionmaker(bind=engine)
session = Session()

# Initialize session state
if "selected_module" not in st.session_state:
    st.session_state.selected_module = None
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "Module Information"

# Organize modules by year
modules_by_year = {
    "Year 1": [
        "Analysis I",
        "Linear Algebra and Group Theory",
        "Calculus and Applications",
        "Probability and Statistics",
        "Introduction to Computation",
        "An Introduction to Applied Maths",
        "M1R Research Project",
    ],
    "Year 2": [
        "Analysis II",
        "M2R Research Project",
        "Linear Algebra and Numerical Analysis",
        "Multivariable Calculus and Differential Equations",
        "Groups and Rings",
        "Lebesgue Measure and Integration",
        "Network Science",
        "PDEs in Action",
        "Principles of Programming",
        "Probability for Statistics",
        "Statistical Modelling 1",
        "i-Explore"
    ],
    "Year 3": {
        "Pure Math": [
            "Probability Theory",
            "Functional Analysis",
            "Fourier Analysis and the Theory of Distributions",
            "Markov Processes",
            "Geometry of Curves and Surfaces",
            "Algebraic Curve",
            "Algebra 3",
            "Group Theory",
            "Galois Theory",
            "Graph Theory",
            "Group Representation Theory",
            "Formalising Mathematics",
            "Number Theory",
            "Algebraic Number Theory",
            "Mathematical Logic",
            "Geometric Complex Analysis"
        ],
        "Applied Math": [
            "Fluid Dynamics 2",
            "Applied Complex Analysis",
            "Bifurcation Theory",
            "Geometric Mechanics",
            "Classical Dynamics",
            "Mathematical Biology",
            "Introduction to Geophysical Fluid Dynamics",
            "Asymptotic Methods",
            "Optimisation",
            "Dynamics of Learning and Iterated Games",
            "Dynamical Systems",
            "Quantum Mechanics 1",
            "Special Relativity and Electromagnetism",
            "Tensor Calculuss and General Relativity",
            "Quantum Mechanics 2",
            "Theory of Partial Differential Equations",
            "Function Spaces and Applications",
            "Advanced Topics in Partial Differential Equations",
            "Finite Elements: Numerical Analysis and Implementation",
            "Computational Dynamical Systems",
            "Computational Linear Algebra",
            "Computational Partial Differential Equations",
            "Methods for Data Science",
            "Scientific Computation",
            "Mathematical Biology 2: Systems Biology",
            "Introduction to Game Theory"

        ],
        "Math Finance": [
            "Mathematical Finance: An Introduction to Option Pricing",
            "Stochastic Differential Equations in Financial Modelling",
            "Rough Paths and Applications to Machine Learning"
        ],
        "Statistics": [
            "Statistical Theory",
            "Applied Statistical Inference",
            "Applied Probability",
            "Time Series Analysis",
            "Stochastic Simulation",
            "Survival Models",
            "Introduction to Statistical Learning",
            "Spatial Statistics",
            "Mathematics of Business and Economics"
        ]
    }
}


## degree info for tab5

degree_info = {
    "G100": {
        "year1": {
            "core_modules": ["Analysis I", "Linear Algebra  and Group Theory","Probability and Statistics","Calculus and Applications","An Introduction to Applied Maths","M1R Research Project"]
        },
        "year2": {
            "core_modules": ["Analysis I", "Linear Algebra  and Group Theory","Probability and Statistics","Calculus and Applications","An Introduction to Applied Maths","M1R Research Project"]
        }
    },
    "G102": {
        "year1": {
            "core_modules": ["Analysis I", "Linear Algebra  and Group Theory","Probability and Statistics","Calculus and Applications","An Introduction to Applied Maths","M1R Research Project"]
        },
        "year2": {
            "core_modules": ["Network Science", "Principles of Programming"],
            "group_b": "Choose 2 modules from Group B"
        }
    },
    "G125": {
        "year1": {
            "core_modules": ["Analysis I", "Linear Algebra  and Group Theory","Probability and Statistics","Calculus and Applications","An Introduction to Applied Maths","M1R Research Project"]
        },
        "year2": {
            "core_modules": ["Groups and Rings", "Lebesgue Measure and Integration"],
            "group_b": "Choose 2 modules from Group B"
        }
    },
    "G1F3": {
        "year1": {
            "core_modules": ["Analysis I", "Linear Algebra  and Group Theory","Probability and Statistics","Calculus and Applications","An Introduction to Applied Maths","M1R Research Project"]
        },
        "year2": {
            "core_modules": ["Partial Differential Equations in Action"],
            "group_b": "Choose 3 modules from Group B"
        }
    },
    "G1G3": {
        "year1": {
            "core_modules": ["Analysis I", "Linear Algebra  and Group Theory","Probability and Statistics","Calculus and Applications","An Introduction to Applied Maths","M1R Research Project"]
        },
        "year2": {
            "core_modules": ["Probability for Statistics", "Statistical Modelling 1"],
            "group_b": "Choose 2 modules from Group B"
        }
    },
    "G1GH": {
        "year1": {
            "core_modules": ["Analysis I", "Linear Algebra  and Group Theory","Probability and Statistics","Calculus and Applications","An Introduction to Applied Maths","M1R Research Project"]
        },
        "year2": {
            "core_modules": ["Probability for Statistics", "Statistical Modelling 1"],
            "group_b": "Choose 2 modules from Group B"
        }
    },
    "GG31": {
        "year1": {
            "core_modules": ["Analysis I", "Linear Algebra  and Group Theory","Probability and Statistics","Calculus and Applications","An Introduction to Applied Maths","M1R Research Project"]
        },
        "year2": {
            "core_modules": ["Probability for Statistics", "Statistical Modelling 1"],
            "group_b": "Choose 2 modules from Group B"
        }
    },
    "G103": {
        "year1": {
           "core_modules": ["Analysis I", "Linear Algebra  and Group Theory","Probability and Statistics","Calculus and Applications","An Introduction to Applied Maths","M1R Research Project"]
        },
        "year2": {
            "group_a": "Choose one module from Group A",
            "group_b": "Choose 4 modules from Group B"
        }
    },
    "G104": {
        "year1": {
            "core_modules": ["Analysis I", "Linear Algebra  and Group Theory","Probability and Statistics","Calculus and Applications","An Introduction to Applied Maths","M1R Research Project"]
        },
        "year2": {
            "group_a": "Choose one module from Group A (language module if required)",
            "group_b": "Choose 4 modules from Group B"
        }
    },
    #Year 2 Module Groups for tab5
    "group_a":{
        "i-Explore"
    },
    "group_b":{
        "Groups and Rings",
        "Lebesgue Measure and Integration",
        "Network Science",
        "PDEs in Action",
        "Principles of Programming",
        "Probability for Statistics",
        "Statistical Modelling 1"
    }
}


def get_modules():
    return session.query(Module).all()

def get_module_by_name(name):
    return session.query(Module).filter_by(name=name).first()

def get_module_by_code(code):
    return session.query(Module).filter_by(code=code).first()



# session state for selected module
if "selected_module" not in st.session_state:
    st.session_state.selected_module = None

#For tab 2 navigate to tab 1
def navigate_to_module(module_name):
    st.session_state.selected_module = module_name
    st.experimental_rerun()


def display_module_details(module_name):
    module = get_module_by_name(module_name)
    if module:
        st.markdown(f"""
        <div style="border: 2px solid #00BFFF; padding: 10px; border-radius: 10px; text-align: left; margin-bottom: 10px; width: 100%;">
            <h3 style="margin-bottom: 10px;">{module.name}</h3>
            <p style="margin-bottom: 5px;"><strong>Code:</strong> {module.code}</p>
            <p style="margin-bottom: 5px;"><strong>Prerequisites:</strong> {module.prerequisites if module.prerequisites else 'None'}</p>
            <p style="margin-bottom: 5px;"><strong>Recommended Prerequisites:</strong> {module.recommended_prerequisites if module.recommended_prerequisites else 'None'}</p>
            <p style="margin-bottom: 5px;"><strong>Summary:</strong> {module.summary if module.summary else 'No summary provided'}</p>
            <p style="margin-bottom: 5px;"><strong>Term:</strong> {module.term if module.term else 'Not specified'}</p>
            <p style="margin-bottom: 5px;"><strong>Lecturer:</strong> {module.lecturer if module.lecturer else 'Not specified'}</p>
            <p style="margin-bottom: 5px;"><strong>Assessments:</strong> {module.assessments if module.assessments else 'No assessment details available'}</p>
            <p style="margin-bottom: 5px;"><strong>Learning Outcomes:</strong> {module.learning_outcome if module.learning_outcome else 'No learning outcomes specified'}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.write("Module not found.")

def get_prerequisites(modules):
    prerequisites = {}
    for module_name in modules:
        module = get_module_by_name(module_name)
        if module:
            # Convert the comma-separated prerequisites string to a list
            prerequisites[module.name] = [p.strip() for p in module.prerequisites.split(',') if p.strip()]
    return prerequisites


## draw module relationship graph with tab3
def draw_module_graph(taken_modules=None, wanted_modules=None):
    G = nx.DiGraph()
    for module in session.query(Module).options(joinedload(Module.keywords)).all():
        G.add_node(module.name)
        # Convert the comma-separated prerequisites string to a list
        prerequisites = [p.strip() for p in module.prerequisites.split(',') if p.strip()]
        for prereq in prerequisites:
            G.add_node(prereq)
            G.add_edge(prereq, module.name)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 7))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray')

    if taken_modules:
        valid_taken_modules = [mod for mod in taken_modules if mod in G.nodes]
        nx.draw_networkx_nodes(G, pos, nodelist=valid_taken_modules, node_color='green')
    if wanted_modules:
        valid_wanted_modules = [mod for mod in wanted_modules if mod in G.nodes]
        nx.draw_networkx_nodes(G, pos, nodelist=valid_wanted_modules, node_color='red')

    plt.title("Module Prerequisite Graph")
    st.pyplot(plt)

# Streamlit UI
st.title("Module Management System")

# Create tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Module Information", "Module Wanted", "Module Relationships", "Assessment Information", "Degree Information"])


with tab1:
    st.header("Module Information by Year")

    # Dropdown for selecting year
    selected_year = st.selectbox("Select Year", options=list(modules_by_year.keys()))
      # Dropdown for selecting term
    selected_term = st.selectbox("Select Term", options=["Autumn", "Spring", "Summer"])

    if selected_year == "Year 3" and selected_term in ["Autumn", "Spring"]:
        # Get categories and modules for Year 3
        year_3_categories = modules_by_year[selected_year]

        for category, modules in year_3_categories.items():
            st.subheader(category)
            filtered_modules = [
                module for module in modules
                if selected_term in (get_module_by_name(module).term if get_module_by_name(module) else '')
            ]

            if filtered_modules:
                for module in filtered_modules:
                    module_name = module  # Get the module name
                    with st.expander(module_name):
                        display_module_details(module_name)
            else:
                st.write(f"No modules available for {selected_term} term in {category}.")

    else:
        # Get modules for the selected year
        modules_for_year = modules_by_year[selected_year]

        # Filter modules based on the selected term
        filtered_modules = [
            module for module in modules_for_year
            if selected_term in (get_module_by_name(module).term if get_module_by_name(module) else '')
        ]

        # Display modules for the selected term
        if filtered_modules:
            for module in filtered_modules:
                module_name = module  
                with st.expander(module_name):
                    display_module_details(module_name)
        else:
            st.write("No modules available for the selected term.")

with tab2:
    st.header("Modules Wanted")
    # User selects desired modules
    desired_modules = st.multiselect("Select the modules you want to take:", options=[module.name for module in get_modules()])

    # Get prerequisites for desired modules
    prerequisites = get_prerequisites(desired_modules)

    # Display prerequisites
    st.subheader("Prerequisites needed:")
    if prerequisites:
        for module, prereqs in prerequisites.items():
            st.markdown(f"""
            <div style="border: 2px solid #FF5733; padding: 10px; border-radius: 10px; text-align: left; margin-bottom: 10px; width: 100%;">
                <h3 style="margin-bottom: 10px;">{module}</h3>
                <p style="margin-bottom: 5px;"><strong>Prerequisites:</strong> {', '.join(prereqs) if prereqs else 'None'}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.write("Select modules to see their prerequisites.")



with tab3:
    st.header("Module Relationships")

    # Dropdown for modules taken
    taken_modules = st.multiselect("Select Modules Taken", options=["None"] + [module.name for module in get_modules()])

    # Dropdown for modules wanted
    wanted_modules = st.multiselect("Select Modules Wanted", options=["None"] + [module.name for module in get_modules()])

    # Validate selections
    if "None" in taken_modules and "None" in wanted_modules:
        st.error("You cannot select 'None' for both modules taken and modules wanted.")
    else:
        # Remove "None" from selections
        if "None" in taken_modules:
            taken_modules.remove("None")
        if "None" in wanted_modules:
            wanted_modules.remove("None")

        # Display the relationships
        draw_module_graph(taken_modules, wanted_modules)


with tab4:
    st.header("Assessment Information")
    st.write("Detailed assessment information will be added here.")


#for tab 5
#mapping of degree codes to full descriptions
degree_descriptions = {
    "G100": "G100 MATHEMATICS (BSc)",
    "G102": "G102 MATHEMATICS WITH MATHEMATICAL COMPUTATION",
    "G103": "G103 MATHEMATICS (MSci)",
    "G104": "G104 MATHEMATICS WITH A YEAR ABROAD (MSci)",
    "G125": "G125 MATHEMATICS (PURE MATHEMATICS)",
    "G1F3": "G1F3 MATHEMATICS WITH APPLIED MATHEMATICS/MATHEMATICAL PHYSICS",
    "G1G3": "G1G3 MATHEMATICS WITH STATISTICS",
    "G1GH": "G1GH MATHEMATICS WITH STATISTICS FOR FINANCE",
    "GG31": "GG31 MATHEMATICS, OPTIMISATION AND STATISTICS"
}



# Reverse the dictionary to get code from description
description_to_code = {v: k for k, v in degree_descriptions.items()}

# Define the degree-specific guide sentences
degree_guides = {
    "G100": "Select one module from Group A and 4 modules from Group B.",
    "G102": "Select one module from Group A. The modules Network Science and Principles of Programming are considered core for this Degree coding and must be taken. Select 2 further modules from Group B.",
    "G125": "Select one module from Group A. The modules Groups and Rings and Lebesgue Measure and Integration are considered core for this Degree coding and must be taken. Select 2 further modules from Group B.",
    "G1F3": "Select one module from Group A. The module Partial Differential Equations in Action is considered core for this Degree coding and must be taken. Select 3 further modules from Group B.",
    "G1G3": "Select one module from Group A. The modules Probability for Statistics and Statistical Modelling I are considered core for this Degree coding and must be taken. Select 2 further modules from Group B.",
    "G1GH": "Select one module from Group A. The modules Probability for Statistics and Statistical Modelling I are considered core for this Degree coding and must be taken. Select 2 further modules from Group B.",
    "GG31": "Select one module from Group A. The modules Probability for Statistics and Statistical Modelling I are considered core for this Degree coding and must be taken. Select 2 further modules from Group B.",
    "G103": "Select one module from Group A and 4 modules from Group B.",
    "G104": "Select one module from Group A (if you are required to take a language module, this must be taken as your Group A module and will be considered core. It will have zero weighting and be worth 7.5 ECTS) and 4 modules from Group B."
}





# Reverse dictionary to get code from description
description_to_code = {v: k for k, v in degree_descriptions.items()}

# Define module information for each degree and year
degree_info = {
    "G100": {
        "Year 2": {
            "group_a": ["i-Explore"],
            "group_b": [ "Lebesgue Measure and Integration", "Network Science","PDEs in Action","Principles of Programming","Probability for Statistics", "Statistical Modelling 1"],
            "guideline": "Select one module from Group A and 4 modules from Group B."
        }
    },
    "G102": {
        "Year 2": {
            "group_a": ["i-Explore"],
            "group_b": [ "Lebesgue Measure and Integration", "Network Science","PDEs in Action","Principles of Programming","Probability for Statistics", "Statistical Modelling 1"],
            "guideline": ("Select one module from Group A. The modules Network Science and Principles of Programming are considered core for this Degree coding and must be taken. Select 2 further modules from Group B.")
        }
    },
    "G103": {
        "Year 2": {
            "group_a": ["i-Explore"],
            "group_b": [ "Lebesgue Measure and Integration", "Network Science","PDEs in Action","Principles of Programming","Probability for Statistics", "Statistical Modelling 1"],
            "guideline": degree_guides["G103"]
        }
    },
    "G104": {
        "Year 2": {
            "group_a": ["i-Explore"],
            "group_b": [ "Lebesgue Measure and Integration", "Network Science","PDEs in Action","Principles of Programming","Probability for Statistics", "Statistical Modelling 1"],
            "guideline": degree_guides["G104"]
        }
    },
    "G125": {
        "Year 2": {
            "group_a": ["i-Explore"],
            "group_b": [ "Lebesgue Measure and Integration", "Network Science","PDEs in Action","Principles of Programming","Probability for Statistics", "Statistical Modelling 1"],
            "guideline": degree_guides["G125"]
        }
    },
    "G1F3": {
        "Year 2": {
            "group_a": ["i-Explore"],
            "group_b": [ "Lebesgue Measure and Integration", "Network Science","PDEs in Action","Principles of Programming","Probability for Statistics", "Statistical Modelling 1"],
            "guideline": degree_guides["G1F3"]
        }
    },
    "G1G3": {
        "Year 2": {
            "group_a": ["i-Explore"],
            "group_b": [ "Lebesgue Measure and Integration", "Network Science","PDEs in Action","Principles of Programming","Probability for Statistics", "Statistical Modelling 1"],
            "guideline": degree_guides["G1G3"]
        }
    },
    "G1GH": {
        "Year 2": {
            "group_a": ["i-Explore"],
            "group_b": [ "Lebesgue Measure and Integration", "Network Science","PDEs in Action","Principles of Programming","Probability for Statistics", "Statistical Modelling 1"],
            "guideline": degree_guides["G1GH"]
    },
    "GG31": {
        "Year 2": {
            "group_a": ["i-Explore"],
            "group_b": [ "Lebesgue Measure and Integration", "Network Science","PDEs in Action","Principles of Programming","Probability for Statistics", "Statistical Modelling 1"],
            "guideline": degree_guides["GG31"]
        }
    }
        }
}
with tab5:
    st.header("Degree Information")

    # Dropdown for degree selection with full descriptions
    selected_description = st.selectbox(
        "Select Degree",
        options=list(degree_descriptions.values())
    )

    # Get the degree code from the selected description
    degree = description_to_code.get(selected_description, "")

    # Dropdown for year selection
    year = st.selectbox("Select Year", ["Year 1", "Year 2", "Year 3", "Year 4"])

    if degree and year:
        st.header(f"{degree} - {year}")

        # Display group modules and guideline for Year 2
        if year == "Year 2":
            st.subheader("Compulsory Modules")
            st.write(f"- Analysis II")
            st.write(f"- Linear Algebra and Numerical Analysis")
            st.write(f"- Multivariable Calculus and Differential Equations")
            if degree in degree_info and "Year 2" in degree_info[degree]:
                group_a_modules = degree_info[degree]["Year 2"].get("group_a", [])
                group_b_modules = degree_info[degree]["Year 2"].get("group_b", [])
                guideline = degree_info[degree]["Year 2"].get("guideline", "")

                # Display Group A and Group B modules
                st.subheader("Group A Modules")
                for module in group_a_modules:
                    st.write(f"- {module}")

                st.subheader("Group B Modules")
                for module in group_b_modules:
                    st.write(f"- {module}")

                # Display the guideline
                st.subheader("Module Selection Guideline")
                st.write(guideline)


        # Display modules available in the selected year
        if year in modules_by_year:
            st.subheader(f"Modules Available in {year}")
            for module in modules_by_year[year]:
                display_module_details(module)