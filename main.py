import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import joinedload
from models import Base, Module, Keyword  # Ensure your models are in a file named `models.py`
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, Table, ForeignKey
from sqlalchemy.orm import relationship


# Database setup
engine = create_engine('sqlite:///modules.db')
Session = sessionmaker(bind=engine)
session = Session()




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
        "Fluid Dynamics 2",
        "Introduction to Geophysical Fluid Dynamics",
        "Fluid Dynamics 1",
        "Asymptotic Methods",
        "Optimisation",
        "Applied Complex Analysis",
        "Dynamics of Learning and Iterated Games",
        "Dynamical Systems",
        "Bifurcation Theory",
        "Geometric Mechanics",
        "Classical Dynamics",
        "Mathematical Biology",
        "Quantum Mechanics 1"
    ]
}

# Degree information
degree_info = {
    "G100": {
        "year1": {
            "group_a": "Choose one module from Group A",
            "group_b": "Choose 4 modules from Group B"
        },
        "year2": {
            "group_a": "Choose one module from Group A",
            "group_b": "Choose 4 modules from Group B"
        }
    },
    "G102": {
        "year1": {
            "group_a": "Choose one module from Group A",
            "group_b": "Choose 4 modules from Group B"
        },
        "year2": {
            "core_modules": ["Network Science", "Principles of Programming"],
            "group_b": "Choose 2 modules from Group B"
        }
    },
    "G125": {
        "year1": {
            "group_a": "Choose one module from Group A",
            "group_b": "Choose 4 modules from Group B"
        },
        "year2": {
            "core_modules": ["Groups and Rings", "Lebesgue Measure and Integration"],
            "group_b": "Choose 2 modules from Group B"
        }
    },
    "G1F3": {
        "year1": {
            "group_a": "Choose one module from Group A",
            "group_b": "Choose 4 modules from Group B"
        },
        "year2": {
            "core_modules": ["Partial Differential Equations in Action"],
            "group_b": "Choose 3 modules from Group B"
        }
    },
    "G1G3": {
        "year1": {
            "group_a": "Choose one module from Group A",
            "group_b": "Choose 4 modules from Group B"
        },
        "year2": {
            "core_modules": ["Probability for Statistics", "Statistical Modelling 1"],
            "group_b": "Choose 2 modules from Group B"
        }
    },
    "G1GH": {
        "year1": {
            "group_a": "Choose one module from Group A",
            "group_b": "Choose 4 modules from Group B"
        },
        "year2": {
            "core_modules": ["Probability for Statistics", "Statistical Modelling 1"],
            "group_b": "Choose 2 modules from Group B"
        }
    },
    "GG31": {
        "year1": {
            "group_a": "Choose one module from Group A",
            "group_b": "Choose 4 modules from Group B"
        },
        "year2": {
            "core_modules": ["Probability for Statistics", "Statistical Modelling 1"],
            "group_b": "Choose 2 modules from Group B"
        }
    },
    "G103": {
        "year1": {
            "group_a": "Choose one module from Group A",
            "group_b": "Choose 4 modules from Group B"
        },
        "year2": {
            "group_a": "Choose one module from Group A",
            "group_b": "Choose 4 modules from Group B"
        }
    },
    "G104": {
        "year1": {
            "group_a": "Choose one module from Group A",
            "group_b": "Choose 4 modules from Group B"
        },
        "year2": {
            "group_a": "Choose one module from Group A (language module if required)",
            "group_b": "Choose 4 modules from Group B"
        }
    }
}

def get_modules():
    return session.query(Module).all()

def get_module_by_name(name):
    return session.query(Module).filter_by(name=name).first()

# Function to display module details
def display_module_details(module_name):
    module = modules_db[module_name]
    st.markdown(f"""
    <div style="border: 2px solid #00BFFF; padding: 10px; border-radius: 10px; text-align: left; margin-bottom: 10px; width: 100%;">
        <h3 style="margin-bottom: 10px;">{module_name}</h3>
        <p style="margin-bottom: 5px;"><strong>Prerequisites:</strong> {', '.join(module['prerequisites']) if module['prerequisites'] else 'None'}</p>
        <p style="margin-bottom: 5px;"><strong>Summary:</strong> {module['summary']}</p>
        <p style="margin-bottom: 5px;"><strong>Term:</strong> {module['term']}</p>
        <p style="margin-bottom: 5px;"><strong>Lecturer:</strong> {module['lecturer']}</p>
        <p style="margin-bottom: 5px;"><strong>Assessments:</strong> {', '.join(module['assessments'])}</p>
    </div>
    """, unsafe_allow_html=True)
    
# Function to find available modules based on completed ones
def find_available_modules(completed_modules):
    available_modules = []
    for module in session.query(Module).all():
        prerequisites = module.prerequisites.split(', ') if module.prerequisites else []
        if module.name not in completed_modules:
            if all(prereq in completed_modules for prereq in prerequisites):
                available_modules.append(module.name)
    return available_modules

# Function to get prerequisites for selected modules
def get_prerequisites(modules):
    prerequisites = {}
    for module_name in modules:
        module = session.query(Module).filter_by(name=module_name).first()
        if module:
            prerequisites[module.name] = module.prerequisites.split(', ') if module.prerequisites else []
    return prerequisites

def draw_module_graph(taken_modules=None, wanted_modules=None):
    G = nx.DiGraph()
    for module in session.query(Module).options(joinedload(Module.keywords)).all():
        G.add_node(module.name)
        prerequisites = module.prerequisites.split(', ') if module.prerequisites else []
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

with tab2:
    st.header("Modules Wanted")
    # User selects desired modules
    desired_modules = st.multiselect("Select the modules you want to take:", options=[module.name for module in session.query(Module).all()])

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



# Tab 1: Module Information by Term
with tab1:
    st.header("Module Information by Year")

    # Dropdown for selecting year
    selected_year = st.selectbox("Select Year", options=list(modules_by_year.keys()))

    # Get modules for the selected year
    modules_for_year = modules_by_year[selected_year]

    # Dropdown for selecting term
    selected_term = st.selectbox("Select Term", options=["Autumn", "Spring", "Summer"])

    # Filter modules based on the selected term
    filtered_modules = [module for module in modules_for_year if selected_term in modules_db[module]["term"]]

    # Display modules for the selected term
    if filtered_modules:
        for module in filtered_modules:
            module_details = modules_db[module]
            st.markdown(f"""
            <div style="border: 2px solid #00BFFF; padding: 10px; border-radius: 10px; text-align: left; margin-bottom: 10px; width: 100%;">
                <h3 style="margin-bottom: 10px;">{module}</h3>
                <p style="margin-bottom: 5px;"><strong>Prerequisites:</strong> {', '.join(module_details['prerequisites']) if module_details['prerequisites'] else 'None'}</p>
                <p style="margin-bottom: 5px;"><strong>Summary:</strong> {module_details['summary']}</p>
                <p style="margin-bottom: 5px;"><strong>Term:</strong> {module_details['term']}</p>
                <p style="margin-bottom: 5px;"><strong>Lecturer:</strong> {module_details['lecturer']}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.write("No modules available for the selected term.")

# Tab 3: Module Relationships
with tab3:
    st.header("Module Relationships")

    # Dropdown for selecting modules taken
    taken_modules = st.multiselect("Select Modules Taken", options=["None"] + list(modules_db.keys()))

    # Dropdown for selecting modules wanted
    wanted_modules = st.multiselect("Select Modules Wanted", options=["None"] + list(modules_db.keys()))

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
        draw_module_graph(modules_db, taken_modules, wanted_modules)


with tab4:
    st.header("Assessment Information")
    st.write("Detailed assessment information will be added here.")

with tab5:
    st.header("Degree Information")

    # Dropdown for degree selection
    degree = st.selectbox("Select Degree", ["G100", "G102", "G103", "G104", "G125", "G1F3", "G1G3", "G1GH", "GG31"])

    # Dropdown for year selection
    year = st.selectbox("Select Year", ["Year 1", "Year 2", "Year 3", "Year 4"])

    if degree and year:
        st.header(f"{degree} - {year}")  # Corrected header format

        # Display degree-specific module selection guidelines
        if degree in degree_info and year in degree_info[degree]:
            st.subheader("Module Selection Guidelines")
            if "core_modules" in degree_info[degree][year]:
                st.write("**Core Modules:**")
                for core_module in degree_info[degree][year]["core_modules"]:
                    st.write(f"- {core_module}")
            if "group_a" in degree_info[degree][year]:
                st.write("**Group A:**")
                st.write(degree_info[degree][year]["group_a"])
            if "group_b" in degree_info[degree][year]:
                st.write("**Group B:**")
                st.write(degree_info[degree][year]["group_b"])

        # Display modules available in the selected year
        if year in modules_by_year:
            st.subheader(f"Modules Available in {year}")
            for module in modules_by_year[year]:
                st.markdown(f"""
                <div style="border: 2px solid #00BFFF; padding: 10px; border-radius: 10px; text-align: left; margin-bottom: 10px; width: 100%;">
                    <h3 style="margin-bottom: 10px;">{module}</h3>
                    <p style="margin-bottom: 5px;"><strong>Prerequisites:</strong> {', '.join(modules_db[module]['prerequisites']) if modules_db[module]['prerequisites'] else 'None'}</p>
                    <p style="margin-bottom: 5px;"><strong>Summary:</strong> {modules_db[module]['summary']}</p>
                    <p style="margin-bottom: 5px;"><strong>Term:</strong> {modules_db[module]['term']}</p>
                    <p style="margin-bottom: 5px;"><strong>Lecturer:</strong> {modules_db[module]['lecturer']}</p>
                    <p style="margin-bottom: 5px;"><strong>Type:</strong> {modules_db[module]['type']}</p>
                </div>
                """, unsafe_allow_html=True)

