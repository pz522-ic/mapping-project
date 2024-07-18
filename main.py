import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import openai






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

# Function to draw a graph of module relationships
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


# Function to handle chatbot responses
def get_chatbot_response(user_input):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Q: {user_input}\nA:",
        max_tokens=150,
        n=1,
        stop=["\n", "Q:"],
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Commonly asked questions and answers
faq = {
    "Can I switch to another programme?": "You can switch to any math programme (excluding JMC) during the first year and second year by filling in a form with the undergraduate office.",
    "Can I drop an optional module halfway?": "You cannot drop an optional module halfway through the term. You must complete the module once you have started it.",
    "How do I contact the undergraduate office?": "You can contact the undergraduate office via email at undergrad.math@university.edu or visit their office on the first floor of the math department building."
}

# Streamlit UI
st.title("Module Management System")

# Create tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Module Information", "Modules Wanted", "Module Relationships", "Assessment Information", "Degree Information", "More Info"])

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

with tab3:
    st.header("Module Relationships")
    st.write("The following graph shows the relationships and prerequisites between modules.")
    draw_module_graph(modules_db)

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
with tab6:
    st.header("More Info")

    # Display commonly asked questions
    st.subheader("Frequently Asked Questions")
    for question, answer in faq.items():
        with st.expander(question):
            st.write(answer)

    # Chatbot interface
    st.subheader("Ask a Question")
    user_query = st.text_input("Type your question here:")
    if user_query:
        response = get_chatbot_response(user_query)
        st.write("**Response:**", response)
