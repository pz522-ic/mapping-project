from sqlalchemy import Column, Integer, String, Text, Table, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

# Association table 
module_keywords = Table('module_keywords', Base.metadata,
    Column('module_id', Integer, ForeignKey('modules.id'), primary_key=True),
    Column('keyword_id', Integer, ForeignKey('keywords.id'), primary_key=True)
)

class Module(Base):
    __tablename__ = 'modules'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    code = Column(String, unique=True, nullable=False)
    prerequisites = Column(Text, nullable=True)
    recommended_prerequisites = Column(Text, nullable=True)
    summary = Column(Text, nullable=True)
    term = Column(String, nullable=False)
    lecturer = Column(String, nullable=False)
    assessments = Column(Text, nullable=True)
    learning_outcome = Column(Text, nullable=True)
    keywords = relationship('Keyword', secondary=module_keywords, back_populates='modules')

class Keyword(Base):
    __tablename__ = 'keywords'
    id = Column(Integer, primary_key=True)
    keyword = Column(String, unique=True, nullable=False)
    modules = relationship('Module', secondary=module_keywords, back_populates='keywords')

# database engine & session
engine = create_engine('sqlite:///modules.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
