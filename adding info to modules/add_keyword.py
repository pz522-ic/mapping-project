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

# Example
add_keyword(session, "Algebraic Topology", "homotopic")
