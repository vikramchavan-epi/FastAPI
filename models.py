from cgitb import strong
from enum import unique
import string
from database import Base
from sqlalchemy import Column,Integer,String

class Users(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True,index=True)
    name=Column(String(50))
    email=Column(String(100),unique=True)
    password=Column(String(100))

