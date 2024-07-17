import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

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
        "prerequisites": ["Mathematics I"],
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
        "prerequisites": ["Physics I"],
        "summary": "Continuation of Physics I.",
        "term": "Spring",
        "lecturer": "Dr. Dan Brown",
        "assessments": ["Exam", "Coursework"]
    },
    "Computer Science I": {
        "prerequisites": [],
        "summary": "Introduction to computer science.",
        "term": "Autumn",
        "lecturer": "Dr. Eve Black",
        "assessments": ["Exam", "Coursework"]
    },
    "Computer Science II": {
        "prerequisites": ["Computer Science I"],
        "summary": "Advanced topics in computer science.",
        "term": "Spring",
        "lecturer": "Dr. Frank Green",
        "assessments": ["Exam", "Coursework"]
    },
    "Algorithms": {
        "prerequisites": ["Computer Science I"],
        "summary": "Study of algorithms.",
        "term": "Autumn",
        "lecturer": "Dr. Grace Miller",
        "assessments": ["Exam", "Coursework"]
    },
    "Data Structures": {
        "prerequisites": ["Computer Science I"],
        "summary": "Study of data structures.",
        "term": "Spring",
        "lecturer": "Dr. Henry Wilson",
        "assessments": ["Exam", "Coursework"]
    },
    "Machine Learning": {
        "prerequisites": ["Mathematics II", "Algorithms"],
        "summary": "Introduction to machine learning.",
        "term": "Autumn",
        "lecturer": "Dr. Irene Davis",
        "assessments": ["Exam", "Coursework"]
    },
    "Artificial Intelligence": {
        "prerequisites": ["Data Structures"],
        "summary": "Study of artificial intelligence.",
        "term": "Spring",
        "lecturer": "Dr. Jack Clark",
        "assessments": ["Exam", "Coursework"]
    },
    "Database Systems": {
        "prerequisites": ["Computer Science I"],
        "summary": "Introduction to database systems.",
        "term": "Autumn",
        "lecturer": "Dr. Karen Martinez",
        "assessments": ["Exam", "Coursework"]
    },
}

# Organize modules by year
modules_by_year = {
    "Year 1": ["Analysis I", "Linear Algebra and Groups", "Introduction to University Math"],
    "Year 2": ["Analysis II", "Linear Algebra adn Numerical Analysis", "Computer Science II", "Algorithms", "Data Structures"],
    "Year 3": ["Machine Learning", "Artificial Intelligence", "Database Systems"]
}

def find_available_modules(completed_modules, modules_db):
    available_modules = []
    for module, details in modules_db.items():
        prerequisites = details["prerequisites"]
        if module not in completed_modules:
            if all(prereq in completed_modules for prereq in prerequisites):
                available_modules.append(module)
    return available_modules

def get_prerequisites(modules, modules_db):
    prerequisites = {}
    for module in modules:
        prerequisites[module] = modules_db.get(module, {}).get("prerequisites", [])
    return prerequisites

def draw_module_graph(modules_db):
    G = nx.DiGraph()
    for module, details in modules_db.items():
        for prereq in details["prerequisites"]:
            G.add_edge(prereq, module)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 7))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray')
    plt.title("Module Prerequisite Graph")
    st.pyplot(plt)

# Streamlit UI
st.title("Module Management System")

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["Module Information", "Module Relationships", "Modules Wanted", "Assessment Information"])

with tab1:
    st.header("Module Information by Year")
    # Display modules by year
    for year, modules in modules_by_year.items():
        with st.expander(year):
            for module in modules:
                st.markdown(f"""
                <div style="border: 2px solid #00BFFF; padding: 10px; border-radius: 10px; text-align: left; margin-bottom: 10px; width: 100%;">
                    <h3 style="margin-bottom: 10px;">{module}</h3>
                    <p style="margin-bottom: 5px;"><strong>Prerequisites:</strong> {', '.join(modules_db[module]['prerequisites']) if modules_db[module]['prerequisites'] else 'None'}</p>
                    <p style="margin-bottom: 5px;"><strong>Summary:</strong> {modules_db[module]['summary']}</p>
                    <p style="margin-bottom: 5px;"><strong>Term:</strong> {modules_db[module]['term']}</p>
                    <p style="margin-bottom: 5px;"><strong>Lecturer:</strong> {modules_db[module]['lecturer']}</p>
                </div>
                """, unsafe_allow_html=True)

with tab2:
    st.header("Module Relationships")
    st.write("The following graph shows the relationships and prerequisites between modules.")
    draw_module_graph(modules_db)

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
