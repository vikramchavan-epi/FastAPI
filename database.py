import imp
import sqlite3
from sqlalchemy import create_engine    
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



SQLALCHEMY_DATABASE_URL='sqlite:///./user1.db'

engine=create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})



SessionLocal= sessionmaker(autocommit=False,bind=engine)

Base=declarative_base()