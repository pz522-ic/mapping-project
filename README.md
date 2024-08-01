#Mapping Project 2024



#requirements.txt: specifies the dependencies that are needed to run the project


#To view the database use terminal:
# specify you own path
cd /Users/zhang/Desktop/mapping-project
sqlite3 modules.db
.tables
SELECT * FROM modules;
SELECT * FROM keywords;

##check keywords database 
sqlite3 keywords.db


#execute code:
/Users/zhang/Desktop/mapping-project
python class.py
python add_modules.py


#run website via Streamlit:
cd /Users/zhang/Desktop/mapping-project
conda activate myenv
streamlit run /Users/zhang/Desktop/mapping-project/main.py
or just click on:
https://mapping-project-bjvybwsj4qt7dhgv6qdjvj.streamlit.app

#restart streamlit
streamlit run yourscript.py


##
conda activate myenv
streamlit run /Users/zhang/Desktop/mapping-project/main.py

#database connection check: prints "Database connection is successful." if connection successful.


