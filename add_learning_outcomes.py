def add_learning_outcome(session, module_name, learning_outcome):
    module = session.query(Module).filter_by(name=module_name).first()
    if not module:
        print(f"Module '{module_name}' not found.")
        return
    
    module.learning_outcome = learning_outcome
    session.commit()
    print(f"Learning outcome added to module '{module_name}' successfully.")

# Example 
add_learning_outcome(session, "Algebraic Topology", "Abstract Algebra")
