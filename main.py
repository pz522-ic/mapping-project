import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network

# Sample database of modules
modules_db = {
    "Analysis I": {
        "prerequisites": [],
        "summary": "Introduction to basic concepts in mathematics.",
        "term": "Autumn and Spring",
        "lecturer": "Dr. Alice Smith",
        "assessments": ["Exam", "Coursework"]
    },
    "Linear Algebra and Groups": {
        "prerequisites": [],
        "summary": "Advanced topics in mathematics.",
        "term": "Autumn and Spring",
        "lecturer": "Dr. Bob Jones",
        "assessments": ["Exam", "Coursework"]
    },
    "Introduction to University Math": {
        "prerequisites": [],
        "summary": "Fundamentals of physics.",
        "term": "Autumn",
        "lecturer": "Dr. Carol White",
        "assessments": ["Exam", "Coursework"]
    },
    "Linear Algebra adn Numerical Analysis": {
        "prerequisites": ["Linear Algebra and Groups"],
        "summary": "Continuation of Linear Algebra and Groups",
        "term": "Autumn and Spring",
        "lecturer": "Dr. Dan Brown",
        "assessments": ["Exam", "Coursework"]
    },
    "Analysis II": {
        "prerequisites": [],
        "summary": "Real Analysis and Complex Analysis",
        "term": "Autumn and Spring",
        "lecturer": "Dr. Eve Black",
        "assessments": ["Exam", "Coursework"]
    },
    "Linear Algebra and Numerical Analysis": {
        "prerequisites": ["Linear Algebra and Groups"],
        "summary": "Advanced topics in computer science.",
        "term": "Autumn and Spring",
        "lecturer": "Dr. Frank Green",
        "assessments": ["Exam", "Coursework"]
    },
    "PDE in Action": {
        "prerequisites": [],
        "summary": "Study of algorithms.",
        "term": "Spring",
        "lecturer": "Dr. Grace Miller",
        "assessments": ["Exam", "Coursework"]
    },
    "Groups and Rings": {
        "prerequisites": ["Linear Algebra and Groups"],
        "summary": "Study of data structures.",
        "term": "Spring",
        "lecturer": "Dr. Henry Wilson",
        "assessments": ["Exam", "Coursework"]
    },
    "Algebra III": {
        "prerequisites": ["Mathematics II", "Algorithms"],
        "summary": "Introduction to machine learning.",
        "term": "Autumn",
        "lecturer": "Dr. Irene Davis",
        "assessments": ["Exam", "Coursework"]
    },
    "Galois Theory": {
        "prerequisites": ["Data Structures"],
        "summary": "Study of artificial intelligence.",
        "term": "Spring",
        "lecturer": "Dr. Jack Clark",
        "assessments": ["Exam", "Coursework"]
    },
    "Fluid Dynamics I": {
        "prerequisites": ["Computer Science I"],
        "summary": "Introduction to Fluid Dynamics",
        "term": "Autumn",
        "lecturer": "Dr. Karen Martinez",
        "assessments": ["Exam", "Coursework"]
    },
}

# Function to find available modules based on completed ones
def find_available_modules(completed_modules, modules_db):
    available_modules = []
    for module, details in modules_db.items():
        prerequisites = details["prerequisites"]
        if module not in completed_modules:
            if all(prereq in completed_modules for prereq in prerequisites):
                available_modules.append(module)
    return available_modules

# Function to get prerequisites for selected modules
def get_prerequisites(modules, modules_db):
    prerequisites = {}
    for module in modules:
        prerequisites[module] = modules_db.get(module, {}).get("prerequisites", [])
    return prerequisites

# Function to draw the module graph
def draw_module_graph(modules_db, completed_modules=[], desired_modules=[]):
    G = nx.DiGraph()
    for module, details in modules_db.items():
        for prereq in details["prerequisites"]:
            G.add_edge(prereq, module)

    # Use Pyvis for interactive network visualization
    net = Network(height='750px', width='100%', bgcolor='#222222', font_color='white')
    for node in G.nodes:
        color = 'green' if node in completed_modules else 'red' if node in desired_modules else 'blue'
        net.add_node(node, label=node, color=color)
    for edge in G.edges:
        net.add_edge(edge[0], edge[1])
    
    net.show('module_graph.html')
    st.components.v1.html(open('module_graph.html', 'r').read(), height=750)

# Streamlit UI
st.title("Module Management System")

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["Module Information", "Module Relationships", "Modules Wanted", "Assessment Information"])

# Tab 1: Module Information
with tab1:
    st.header("Module Information by Term")
    term = st.selectbox("Select Term", options=["Autumn", "Spring", "Summer"])
    
    for module, details in modules_db.items():
        if term in details["term"]:
            st.markdown(f"""
            <div style="border: 2px solid #00BFFF; padding: 10px; border-radius: 10px; text-align: left; margin-bottom: 10px; width: 100%;">
                <h3 style="margin-bottom: 10px;">{module}</h3>
                <p style="margin-bottom: 5px;"><strong>Prerequisites:</strong> {', '.join(details['prerequisites']) if details['prerequisites'] else 'None'}</p>
                <p style="margin-bottom: 5px;"><strong>Summary:</strong> {details['summary']}</p>
                <p style="margin-bottom: 5px;"><strong>Term:</strong> {details['term']}</p>
                <p style="margin-bottom: 5px;"><strong>Lecturer:</strong> {details['lecturer']}</p>
                <a href="/{module.replace(' ', '_')}"><button>Go to Module Page</button></a>
            </div>
            """, unsafe_allow_html=True)

# Tab 2: Module Relationships
with tab2:
    st.header("Module Relationships")
    
    completed_modules = st.multiselect("Select completed modules:", options=list(modules_db.keys()))
    desired_modules = st.multiselect("Select desired modules:", options=list(modules_db.keys()))
    
    st.write("The following graph shows the relationships and prerequisites between modules.")
    draw_module_graph(modules_db, completed_modules, desired_modules)

# Tab 3: Modules Wanted
with tab3:
    st.header("Modules Wanted")
    
    # User selects desired modules
    desired_modules = st.multiselect("Select the modules you want to take:", options=list(modules_db.keys()))

    # Get prerequisites for desired modules
    prerequisites = get_prerequisites(desired_modules, modules_db)

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

# Tab 4: Assessment Information
with tab4:
    st.header("Assessment Information")
    
    # Display assessment information for each module
    for module, details in modules_db.items():
        assessments = details.get("assessments", [])
        st.markdown(f"""
        <div style="border: 2px solid #FFD700; padding: 10px; border-radius: 10px; text-align: left; margin-bottom: 10px; width: 100%;">
            <h3 style="margin-bottom: 10px;">{module}</h3>
            <p style="margin-bottom: 5px;"><strong>Assessments:</strong> {', '.join(assessments) if assessments else 'None'}</p>
        </div>
        """, unsafe_allow_html=True)
