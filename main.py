import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from models import Module, Keyword  # Ensure models.py contains these definitions

# Database setup
engine = create_engine('sqlite:///modules.db')
Session = sessionmaker(bind=engine)
session = Session()

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

def get_modules():
    return session.query(Module).all()

def get_module_by_name(name):
    return session.query(Module).filter_by(name=name).first()

def display_module_details(module_name):
    module = get_module_by_name(module_name)
    if module:
        st.markdown(f"""
        <div style="border: 2px solid #00BFFF; padding: 10px; border-radius: 10px; text-align: left; margin-bottom: 10px; width: 100%;">
            <h3 style="margin-bottom: 10px;">{module.name}</h3>
            <p style="margin-bottom: 5px;"><strong>Prerequisites:</strong> {module.prerequisites if module.prerequisites else 'None'}</p>
            <p style="margin-bottom: 5px;"><strong>Summary:</strong> {module.summary}</p>
            <p style="margin-bottom: 5px;"><strong>Term:</strong> {module.term}</p>
            <p style="margin-bottom: 5px;"><strong>Lecturer:</strong> {module.lecturer}</p>
            <p style="margin-bottom: 5px;"><strong>Assessments:</strong> {module.assessments}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.write("Module not found.")

def find_available_modules(completed_modules):
    available_modules = []
    for module in session.query(Module).all():
        prerequisites = module.prerequisites.split(', ') if module.prerequisites else []
        if module.name not in completed_modules:
            if all(prereq in completed_modules for prereq in prerequisites):
                available_modules.append(module.name)
    return available_modules

def get_prerequisites(modules):
    prerequisites = {}
    for module_name in modules:
        module = get_module_by_name(module_name)
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

with tab1:
    st.header("Module Information by Year")

    # Dropdown for selecting year
    selected_year = st.selectbox("Select Year", options=list(modules_by_year.keys()))

    # Get modules for the selected year
    modules_for_year = modules_by_year[selected_year]

    # Dropdown for selecting term
    selected_term = st.selectbox("Select Term", options=["Autumn", "Spring", "Summer","Autumn and Spring"])

    # Filter modules based on the selected term
    filtered_modules = [module for module in modules_for_year if selected_term in (get_module_by_name(module).term if get_module_by_name(module) else '')]

    # Display modules for the selected term
    if filtered_modules:
        for module in filtered_modules:
            display_module_details(module)
    else:
        st.write("No modules available for the selected term.")

with tab3:
    st.header("Module Relationships")

    # Dropdown for selecting modules taken
    taken_modules = st.multiselect("Select Modules Taken", options=["None"] + [module.name for module in get_modules()])

    # Dropdown for selecting modules wanted
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

with tab5:
    st.header("Degree Information")

    # Dropdown for degree selection
    degree = st.selectbox("Select Degree", ["G100", "G102", "G103", "G104", "G125", "G1F3", "G1G3", "G1GH", "GG31"])

    # Dropdown for year selection
    year = st.selectbox("Select Year", ["Year 1", "Year 2", "Year 3", "Year 4"])

    if degree and year:
        st.header(f"{degree} - {year}")

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
                display_module_details(module)

