from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from galeria import settings

DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))

def create_posts_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class Rest_Posts(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "rest_posts"

    id = Column(Integer, primary_key=True)
    text = Column('text', String)
#    url = Column('link', String)
#    date = Column('date', String)
