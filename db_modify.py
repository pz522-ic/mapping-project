from module_class import Module, Keyword

def add_keyword(session, module_name, keyword):
    module = session.query(Module).filter_by(name=module_name).first()
    if not module:
        print(f"Module '{module_name}' not found.")
        return
    
    existing_keyword = session.query(Keyword).filter_by(keyword=keyword).first()
    if existing_keyword:
        keyword_obj = existing_keyword
    else:
        keyword_obj = Keyword(keyword=keyword)
        session.add(keyword_obj)
    
    module.keywords.append(keyword_obj)
    session.commit()
    print(f"Keyword '{keyword}' added to module '{module_name}' successfully.")

def add_learning_outcome(session, module_name, learning_outcome):
    module = session.query(Module).filter_by(name=module_name).first()
    if not module:
        print(f"Module '{module_name}' not found.")
        return
    
    module.learning_outcome = learning_outcome
    session.commit()
    print(f"Learning outcome added to module '{module_name}' successfully.")  

def add_module(session, name, code, prerequisites, recommended_prerequisites, term, lecturer, assessments):
    prerequisites_str = ', '.join(prerequisites) if prerequisites else ""
    assessments_str = ', '.join(assessments) if assessments else ""
    
    new_module = Module(
        name=name,
        code=code,
        prerequisites=prerequisites_str,
        recommended_prerequisites=recommended_prerequisites,
        term=term,
        lecturer=lecturer,
        assessments=assessments_str
    )
    
    session.add(new_module)
    session.commit()
    print(f"Module '{name}' added successfully.")\
    
def add_summary(session, module_name, summary):
    module = session.query(Module).filter_by(name=module_name).first()
    if not module:
        print(f"Module '{module_name}' not found.")
        return
    
    module.summary = summary
    session.commit()
    print(f"Summary added to module '{module_name}' successfully.")