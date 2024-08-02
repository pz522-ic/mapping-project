def add_summary(session, module_name, summary):
    module = session.query(Module).filter_by(name=module_name).first()
    if not module:
        print(f"Module '{module_name}' not found.")
        return
    
    module.summary = summary
    session.commit()
    print(f"Summary added to module '{module_name}' successfully.")

# Example
add_summary(session, "Algebraic Topology", "This course covers .....")
