import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# Sample database of modules
modules_db = {
    "Mathematics I": {
        "prerequisites": [],
        "summary": "Introduction to basic concepts in mathematics.",
        "term": "Autumn",
        "lecturer": "Dr. Alice Smith"
    },
    "Mathematics II": {
        "prerequisites": ["Mathematics I"],
        "summary": "Advanced topics in mathematics.",
        "term": "Spring",
        "lecturer": "Dr. Bob Jones"
    },
    "Physics I": {
        "prerequisites": [],
        "summary": "Fundamentals of physics.",
        "term": "Autumn",
        "lecturer": "Dr. Carol White"
    },
    "Physics II": {
        "prerequisites": ["Physics I"],
        "summary": "Continuation of Physics I.",
        "term": "Spring",
        "lecturer": "Dr. Dan Brown"
    },
    "Computer Science I": {
        "prerequisites": [],
        "summary": "Introduction to computer science.",
        "term": "Autumn",
        "lecturer": "Dr. Eve Black"
    },
    "Computer Science II": {
        "prerequisites": ["Computer Science I"],
        "summary": "Advanced topics in computer science.",
        "term": "Spring",
        "lecturer": "Dr. Frank Green"
    },
    "Algorithms": {
        "prerequisites": ["Computer Science I"],
        "summary": "Study of algorithms.",
        "term": "Autumn",
        "lecturer": "Dr. Grace Miller"
    },
    "Data Structures": {
        "prerequisites": ["Computer Science I"],
        "summary": "Study of data structures.",
        "term": "Spring",
        "lecturer": "Dr. Henry Wilson"
    },
    "Machine Learning": {
        "prerequisites": ["Mathematics II", "Algorithms"],
        "summary": "Introduction to machine learning.",
        "term": "Autumn",
        "lecturer": "Dr. Irene Davis"
    },
    "Artificial Intelligence": {
        "prerequisites": ["Data Structures"],
        "summary": "Study of artificial intelligence.",
        "term": "Spring",
        "lecturer": "Dr. Jack Clark"
    },
    "Database Systems": {
        "prerequisites": ["Computer Science I"],
        "summary": "Introduction to database systems.",
        "term": "Autumn",
        "lecturer": "Dr. Karen Martinez"
    },
}

# Organize modules by year
modules_by_year = {
    "Year 1": ["Mathematics I", "Physics I", "Computer Science I"],
    "Year 2": ["Mathematics II", "Physics II", "Computer Science II", "Algorithms", "Data Structures"],
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
tab1, tab2, tab3, tab4 = st.tabs(["Modules Completed", "Modules Wanted", "Module Information", "Module Relationships"])

with tab1:
    st.header("Modules Completed")
    # User selects completed modules
    completed_modules = st.multiselect("Select the modules you have completed:", options=list(modules_db.keys()))

    # Find available modules based on completed modules
    available_modules = find_available_modules(completed_modules, modules_db)

    # Display available modules
    st.subheader("Modules you can take next:")
    if available_modules:
        for module in available_modules:
            st.markdown(f"""
            <div style="border: 2px solid #4CAF50; padding: 10px; border-radius: 10px; text-align: left; margin-bottom: 10px; width: 100%;">
                <h3 style="margin-bottom: 10px;">{module}</h3>
                <p style="margin-bottom: 5px;">{modules_db[module]['summary']}</p>
                <p style="margin-bottom: 5px;"><strong>Term:</strong> {modules_db[module]['term']}</p>
                <p style="margin-bottom: 5px;"><strong>Lecturer:</strong> {modules_db[module]['lecturer']}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.write("No available modules based on your current selections.")

with tab2:
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

with tab3:
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

with tab4:
    st.header("Module Relationships")
    st.write("The following graph shows the relationships and prerequisites between modules.")
    draw_module_graph(modules_db)
