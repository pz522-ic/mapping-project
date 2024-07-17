import streamlit as st

# Define module database
modules_db = {
    "Introduction to University Math (MATH40001/40009)": {
        "prerequisites": [],
        "summary": "Introduction to university-level mathematics.",
        "term": "Autumn",
        "lecturer": "John Smith",
        "assessments": ["Exam"],
        "type": "Core"
    },
    "Analysis I (MATH40002)": {
        "prerequisites": ["Introduction to University Math (MATH40001/40009)"],
        "summary": "Introduction to analysis and calculus.",
        "term": "Spring",
        "lecturer": "Emma Johnson",
        "assessments": ["Exam", "Coursework"],
        "type": "Core"
    },
    "Linear Algebra and Group Theory (MATH40003)": {
        "prerequisites": ["Introduction to University Math (MATH40001/40009)"],
        "summary": "Fundamentals of linear algebra and group theory.",
        "term": "Autumn",
        "lecturer": "Michael Brown",
        "assessments": ["Exam", "Coursework"],
        "type": "Core"
    },
    "Calculus and Applications (MATH40004)": {
        "prerequisites": ["Introduction to University Math (MATH40001/40009)"],
        "summary": "Advanced calculus techniques and their applications.",
        "term": "Spring",
        "lecturer": "Sophia Wilson",
        "assessments": ["Exam", "Coursework"],
        "type": "Core"
    },
    "Probability and Statistics (MATH40005)": {
        "prerequisites": ["Introduction to University Math (MATH40001/40009)"],
        "summary": "Introduction to probability theory and statistical methods.",
        "term": "Autumn",
        "lecturer": "David Thompson",
        "assessments": ["Exam", "Coursework"],
        "type": "Core"
    },
    "Introduction to Computation (MATH40006)": {
        "prerequisites": ["Introduction to University Math (MATH40001/40009)"],
        "summary": "Introduction to computational mathematics.",
        "term": "Spring",
        "lecturer": "Olivia Martinez",
        "assessments": ["Exam", "Coursework"],
        "type": "Core"
    },
    "An Introduction to Applied Maths (MATH40007)": {
        "prerequisites": ["Introduction to University Math (MATH40001/40009)"],
        "summary": "Applications of mathematics in various fields.",
        "term": "Autumn",
        "lecturer": "Ethan Davis",
        "assessments": ["Exam", "Coursework"],
        "type": "Core"
    },
    "M1R (MATH40008)": {
        "prerequisites": ["Introduction to University Math (MATH40001/40009)"],
        "summary": "Mathematical reasoning and proof techniques.",
        "term": "Spring",
        "lecturer": "Isabella Clark",
        "assessments": ["Exam", "Coursework"],
        "type": "Core"
    },
    "Linear Algebra (JMC) (MATH40012)": {
        "prerequisites": ["Introduction to University Math (MATH40001/40009)"],
        "summary": "Linear algebra taught in the Joint Mathematics Centre.",
        "term": "Autumn",
        "lecturer": "James Lee",
        "assessments": ["Exam", "Coursework"],
        "type": "Core"
    },
    "Analysis 2: Real Analysis and Topology (MATH50001/50017)": {
        "prerequisites": ["Analysis I (MATH40002)"],
        "summary": "Advanced real analysis and topology.",
        "term": "Spring",
        "lecturer": "Rachel Green",
        "assessments": ["Exam", "Coursework"],
        "type": "Optional"
    },
    "Analysis 2: Complex Analysis (MATH50001/50018)": {
        "prerequisites": ["Analysis I (MATH40002)"],
        "summary": "Advanced complex analysis techniques.",
        "term": "Autumn",
        "lecturer": "Monica Geller",
        "assessments": ["Exam", "Coursework"],
        "type": "Optional"
    },
    "M2R (MATH50002/MATH50014)": {
        "prerequisites": ["Analysis I (MATH40002)"],
        "summary": "Research methods in mathematics.",
        "term": "Spring",
        "lecturer": "Ross Geller",
        "assessments": ["Exam", "Coursework"],
        "type": "Optional"
    },
    "Linear Algebra (MATH50003/50012)": {
        "prerequisites": ["Linear Algebra and Group Theory (MATH40003)"],
        "summary": "Advanced linear algebra techniques.",
        "term": "Autumn",
        "lecturer": "Chandler Bing",
        "assessments": ["Exam", "Coursework"],
        "type": "Optional"
    },
    "Numerical Analysis (MATH50003/50016)": {
        "prerequisites": ["Linear Algebra and Group Theory (MATH40003)"],
        "summary": "Numerical methods in mathematical analysis.",
        "term": "Spring",
        "lecturer": "Phoebe Buffay",
        "assessments": ["Exam", "Coursework"],
        "type": "Optional"
    },
    "Multivariable Calculus (MATH50004/50015)": {
        "prerequisites": ["Calculus and Applications (MATH40004)"],
        "summary": "Advanced calculus in multiple dimensions.",
        "term": "Autumn",
        "lecturer": "Joey Tribbiani",
        "assessments": ["Exam", "Coursework"],
        "type": "Optional"
    },
    "Differential Equations (MATH50004/50019)": {
        "prerequisites": ["Calculus and Applications (MATH40004)"],
        "summary": "Advanced differential equations.",
        "term": "Spring",
        "lecturer": "Rachel Green",
        "assessments": ["Exam", "Coursework"],
        "type": "Optional"
    },
    "Groups and Rings (MATH50005)": {
        "prerequisites": ["Linear Algebra and Group Theory (MATH40003)"],
        "summary": "Group theory and ring theory.",
        "term": "Autumn",
        "lecturer": "Monica Geller",
        "assessments": ["Exam", "Coursework"],
        "type": "Optional"
    },
    "Lebesgue Measure and Integration (MATH50006)": {
        "prerequisites": ["Analysis 2: Real Analysis and Topology (MATH50001/50017)"],
        "summary": "Advanced measure theory and integration.",
        "term": "Spring",
        "lecturer": "Ross Geller",
        "assessments": ["Exam", "Coursework"],
        "type": "Optional"
    },
    "Network Science (MATH50007)": {
        "prerequisites": ["Analysis 2: Real Analysis and Topology (MATH50001/50017)"],
        "summary": "Introduction to network science.",
        "term": "Autumn",
        "lecturer": "Chandler Bing",
        "assessments": ["Exam", "Coursework"],
        "type": "Optional"
    },
    "PDEs in Action (MATH50008)": {
        "prerequisites": ["Differential Equations (MATH50004/50019)"],
        "summary": "Applications of partial differential equations.",
        "term": "Spring",
        "lecturer": "Phoebe Buffay",
        "assessments": ["Exam", "Coursework"],
        "type": "Optional"
    },
    "Principles of Programming (MATH50009)": {
        "prerequisites": ["Introduction to Computation (MATH40006)"],
        "summary": "Fundamentals of programming principles.",
        "term": "Autumn",
        "lecturer": "Joey Tribbiani",
        "assessments": ["Exam", "Coursework"],
        "type": "Optional"
    },
    "Probability for Statistics (MATH50010)": {
        "prerequisites": ["Probability and Statistics (MATH40005)"],
        "summary": "Probability theory for statistical applications.",
        "term": "Spring",
        "lecturer": "Rachel Green",
        "assessments": ["Exam", "Coursework"],
        "type": "Optional"
    },
    "Statistical Modelling 1 (MATH50011)": {
        "prerequisites": ["Probability and Statistics (MATH40005)"],
        "summary": "Statistical modeling techniques.",
        "term": "Autumn",
        "lecturer": "Monica Geller",
        "assessments": ["Exam", "Coursework"],
        "type": "Optional"
    },
    "Probability (JMC) (MATH50013)": {
        "prerequisites": ["Probability and Statistics (MATH40005)"],
        "summary": "Probability theory taught in the Joint Mathematics Centre.",
        "term": "Spring",
        "lecturer": "Ross Geller",
        "assessments": ["Exam", "Coursework"],
        "type": "Optional"
    }
}

# Define module categories by year
modules_by_year = {
    "Year 1": ["Introduction to University Math (MATH40001/40009)", "Analysis I (MATH40002)", "Linear Algebra and Group Theory (MATH40003)", "Calculus and Applications (MATH40004)", "Probability and Statistics (MATH40005)", "Introduction to Computation (MATH40006)", "An Introduction to Applied Maths (MATH40007)", "M1R (MATH40008)", "Linear Algebra (JMC) (MATH40012)"],
    "Year 2": ["Analysis 2: Real Analysis and Topology (MATH50001/50017)", "Analysis 2: Complex Analysis (MATH50001/50018)", "M2R (MATH50002/MATH50014)", "Linear Algebra (MATH50003/50012)", "Numerical Analysis (MATH50003/50016)", "Multivariable Calculus (MATH50004/50015)", "Differential Equations (MATH50004/50019)", "Groups and Rings (MATH50005)", "Lebesgue Measure and Integration (MATH50006)", "Network Science (MATH50007)", "PDEs in Action (MATH50008)", "Principles of Programming (MATH50009)", "Probability for Statistics (MATH50010)", "Statistical Modelling 1 (MATH50011)"]
}

# Define degree information
degrees_info = {
    "G100": {
        "Year 2": {
            "Group A": ["Analysis 2: Real Analysis and Topology (MATH50001/50017)", "Groups and Rings (MATH50005)"],
            "Group B": ["Analysis 2: Complex Analysis (MATH50001/50018)", "M2R (MATH50002/MATH50014)", "Linear Algebra (MATH50003/50012)", "Numerical Analysis (MATH50003/50016)", "Multivariable Calculus (MATH50004/50015)", "Differential Equations (MATH50004/50019)", "Lebesgue Measure and Integration (MATH50006)", "Network Science (MATH50007)", "PDEs in Action (MATH50008)", "Principles of Programming (MATH50009)", "Probability for Statistics (MATH50010)", "Statistical Modelling 1 (MATH50011)"],
            "Core": ["Probability for Statistics (MATH50010)", "Statistical Modelling 1 (MATH50011)"]
        }
    },
    "G102": {
        "Year 2": {
            "Group A": ["Analysis 2: Real Analysis and Topology (MATH50001/50017)", "Network Science (MATH50007)"],
            "Group B": ["Analysis 2: Complex Analysis (MATH50001/50018)", "M2R (MATH50002/MATH50014)", "Linear Algebra (MATH50003/50012)", "Numerical Analysis (MATH50003/50016)", "Multivariable Calculus (MATH50004/50015)", "Differential Equations (MATH50004/50019)", "Lebesgue Measure and Integration (MATH50006)", "PDEs in Action (MATH50008)", "Principles of Programming (MATH50009)", "Probability for Statistics (MATH50010)", "Statistical Modelling 1 (MATH50011)"],
            "Core": ["Network Science (MATH50007)", "Principles of Programming (MATH50009)"]
        }
    },
    "G125": {
        "Year 2": {
            "Group A": ["Analysis 2: Real Analysis and Topology (MATH50001/50017)", "Lebesgue Measure and Integration (MATH50006)"],
            "Group B": ["Analysis 2: Complex Analysis (MATH50001/50018)", "M2R (MATH50002/MATH50014)", "Linear Algebra (MATH50003/50012)", "Numerical Analysis (MATH50003/50016)", "Multivariable Calculus (MATH50004/50015)", "Differential Equations (MATH50004/50019)", "Network Science (MATH50007)", "PDEs in Action (MATH50008)", "Principles of Programming (MATH50009)", "Probability for Statistics (MATH50010)", "Statistical Modelling 1 (MATH50011)"],
            "Core": ["Lebesgue Measure and Integration (MATH50006)", "Groups and Rings (MATH50005)"]
        }
    },
    "G1F3": {
        "Year 2": {
            "Group A": ["Analysis 2: Real Analysis and Topology (MATH50001/50017)", "Partial Differential Equations in Action (MATH50008)"],
            "Group B": ["Analysis 2: Complex Analysis (MATH50001/50018)", "M2R (MATH50002/MATH50014)", "Linear Algebra (MATH50003/50012)", "Numerical Analysis (MATH50003/50016)", "Multivariable Calculus (MATH50004/50015)", "Differential Equations (MATH50004/50019)", "Lebesgue Measure and Integration (MATH50006)", "Network Science (MATH50007)", "Principles of Programming (MATH50009)", "Probability for Statistics (MATH50010)", "Statistical Modelling 1 (MATH50011)"],
            "Core": ["Partial Differential Equations in Action (MATH50008)"]
        }
    },
    "G1G3": {
        "Year 2": {
            "Group A": ["Analysis 2: Real Analysis and Topology (MATH50001/50017)", "Probability for Statistics (MATH50010)"],
            "Group B": ["Analysis 2: Complex Analysis (MATH50001/50018)", "M2R (MATH50002/MATH50014)", "Linear Algebra (MATH50003/50012)", "Numerical Analysis (MATH50003/50016)", "Multivariable Calculus (MATH50004/50015)", "Differential Equations (MATH50004/50019)", "Lebesgue Measure and Integration (MATH50006)", "Network Science (MATH50007)", "PDEs in Action (MATH50008)", "Principles of Programming (MATH50009)", "Statistical Modelling 1 (MATH50011)"],
            "Core": ["Probability for Statistics (MATH50010)", "Statistical Modelling 1 (MATH50011)"]
        }
    },
    "G1GH": {
        "Year 2": {
            "Group A": ["Analysis 2: Real Analysis and Topology (MATH50001/50017)", "Probability for Statistics (MATH50010)"],
            "Group B": ["Analysis 2: Complex Analysis (MATH50001/50018)", "M2R (MATH50002/MATH50014)", "Linear Algebra (MATH50003/50012)", "Numerical Analysis (MATH50003/50016)", "Multivariable Calculus (MATH50004/50015)", "Differential Equations (MATH50004/50019)", "Lebesgue Measure and Integration (MATH50006)", "Network Science (MATH50007)", "PDEs in Action (MATH50008)", "Principles of Programming (MATH50009)", "Statistical Modelling 1 (MATH50011)"],
            "Core": ["Probability for Statistics (MATH50010)", "Statistical Modelling 1 (MATH50011)"]
        }
    },
    "GG31": {
        "Year 2": {
            "Group A": ["Analysis 2: Real Analysis and Topology (MATH50001/50017)", "Probability for Statistics (MATH50010)"],
            "Group B": ["Analysis 2: Complex Analysis (MATH50001/50018)", "M2R (MATH50002/MATH50014)", "Linear Algebra (MATH50003/50012)", "Numerical Analysis (MATH50003/50016)", "Multivariable Calculus (MATH50004/50015)", "Differential Equations (MATH50004/50019)", "Lebesgue Measure and Integration (MATH50006)", "Network Science (MATH50007)", "PDEs in Action (MATH50008)", "Principles of Programming (MATH50009)", "Statistical Modelling 1 (MATH50011)"],
            "Core": ["Probability for Statistics (MATH50010)", "Statistical Modelling 1 (MATH50011)"]
        }
    },
    "G103": {
        "Year 2": {
            "Group A": ["Analysis 2: Real Analysis and Topology (MATH50001/50017)", "Groups and Rings (MATH50005)"],
            "Group B": ["Analysis 2: Complex Analysis (MATH50001/50018)", "M2R (MATH50002/MATH50014)", "Linear Algebra (MATH50003/50012)", "Numerical Analysis (MATH50003/50016)", "Multivariable Calculus (MATH50004/50015)", "Differential Equations (MATH50004/50019)", "Lebesgue Measure and Integration (MATH50006)", "Network Science (MATH50007)", "PDEs in Action (MATH50008)", "Principles of Programming (MATH50009)", "Probability for Statistics (MATH50010)", "Statistical Modelling 1 (MATH50011)"],
            "Core": ["Probability for Statistics (MATH50010)", "Statistical Modelling 1 (MATH50011)"]
        }
    },
    "G104": {
        "Year 2": {
            "Group A": ["Analysis 2: Real Analysis and Topology (MATH50001/50017)", "Probability (JMC) (MATH50013)"],
            "Group B": ["Analysis 2: Complex Analysis (MATH50001/50018)", "M2R (MATH50002/MATH50014)", "Linear Algebra (MATH50003/50012)", "Numerical Analysis (MATH50003/50016)", "Multivariable Calculus (MATH50004/50015)", "Differential Equations (MATH50004/50019)", "Lebesgue Measure and Integration (MATH50006)", "Network Science (MATH50007)", "PDEs in Action (MATH50008)", "Principles of Programming (MATH50009)", "Statistical Modelling 1 (MATH50011)"],
            "Core": ["Probability (JMC) (MATH50013)", "Statistical Modelling 1 (MATH50011)"]
        }
    }
}

# Main content
st.title("Mathematics Degree Information")

# Sidebar navigation
menu_options = ["Home", "Assessment Information", "Module Wanted", "Module Taken"]
menu_choice = st.sidebar.selectbox("Select an option", menu_options)

# Home page
if menu_choice == "Home":
    st.header("Welcome to Mathematics Degree Information")
    st.subheader("Choose a tab to view information.")

# Assessment Information tab
elif menu_choice == "Assessment Information":
    st.header("Assessment Information")
    st.write("Here you can find assessment details for various modules.")
    selected_module = st.selectbox("Select a module", list(modules_db.keys()))
    st.subheader(f"Assessment details for {selected_module}:")
    module_info = modules_db[selected_module]
    st.write(f"Summary: {module_info['summary']}")
    st.write(f"Term: {module_info['term']}")
    st.write(f"Lecturer: {module_info['lecturer']}")
    st.write(f"Assessments: {', '.join(module_info['assessments'])}")
    st.write(f"Type: {module_info['type']}")

# Module Wanted tab
elif menu_choice == "Module Wanted":
    st.header("Module Wanted")
    st.write("Select your desired module based on your degree requirements.")

    # Degree selection
    degree = st.selectbox("Select your degree", ["G100", "G102", "G103", "G104", "G125", "G1F3", "G1G3", "G1GH", "GG31"])

    # Year selection (currently only Year 2 is supported)
    year = "Year 2"

    # Display groups and core modules for the selected degree and year
    if degree in degrees_info and year in degrees_info[degree]:
        st.subheader(f"Degree: {degree}, Year: {year}")
        st.write("Choose modules according to your degree requirements.")

        # Display Group A options
        st.subheader("Group A (Select 1)")
        group_a_selection = st.selectbox("Choose 1 module from Group A", degrees_info[degree][year]["Group A"])

        # Display Group B options
        st.subheader("Group B (Select 4)")
        group_b_selections = st.multiselect("Choose 4 modules from Group B", degrees_info[degree][year]["Group B"])

        # Display core modules
        if "Core" in degrees_info[degree][year]:
            st.subheader("Core Modules")
            core_modules = degrees_info[degree][year]["Core"]
            for core_module in core_modules:
                st.write(core_module)

# Module Taken tab
elif menu_choice == "Module Taken":
    st.header("Module Taken")
    st.write("Here you can view the modules you have already taken.")

    # Example of modules taken (replace with actual data)
    modules_taken = ["Introduction to University Math (MATH40001/40009)", "Analysis I (MATH40002)"]

    if modules_taken:
        st.subheader("Modules Taken:")
        for module in modules_taken:
            st.write(module)
    else:
        st.write("No modules taken yet.")

