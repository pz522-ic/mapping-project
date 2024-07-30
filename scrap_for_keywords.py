import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from module_class import Module, Keyword, Base 

# Database setup
DATABASE_URL = 'sqlite:///modules.db'  
engine = create_engine(DATABASE_URL)
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()

# scrape keywords from the website
def scrape_keywords():
    base_url = "https://blastzit.eu.pythonanywhere.com"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    modules = []
    for link in soup.find_all('a', href=True):
        if "module" in link['href']:
            module_url = f"{base_url}/{link['href']}"
            module_response = requests.get(module_url)
            module_soup = BeautifulSoup(module_response.content, 'html.parser')

            # Extract the module code and keywords
            code_element = module_soup.find(text="Code").find_next()
            keywords_element = module_soup.find(text="Keywords").find_next()

            if code_element and keywords_element:
                code = code_element.get_text(strip=True).replace('MATH', 'M').replace('/', '_')
                keywords = keywords_element.get_text(strip=True).split(',')
                modules.append((code, keywords))

    return modules

# Function to update database with keywords
def update_database(modules):
    for code, keywords in modules:
        # Find the module in the database by code
        module = session.query(Module).filter(Module.code == code).first()
        if module:
            # Add keywords to the module
            for keyword in keywords:
                keyword = keyword.strip()
                existing_keyword = session.query(Keyword).filter(Keyword.keyword == keyword).first()
                if not existing_keyword:
                    # Create new keyword if it doesn't exist
                    new_keyword = Keyword(keyword=keyword)
                    module.keywords.append(new_keyword)
                else:
                    module.keywords.append(existing_keyword)
            session.commit()

# Main function
def main():
    modules = scrape_keywords()
    update_database(modules)

if __name__ == "__main__":
    main()
