# ----------------------------------------------------------------------
# Name:        lecture26
# Purpose:     Demonstrate database access with SQLAlchemy
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Module containing imports to be used in lecture 26

From the Python console, type:
from lecture26 import *
You can also copy and paste the imports into the console.
"""
from sqlalchemy import create_engine, select
from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # Construct a new base class for our mappings


class Student(Base):

    """
    Class to be used in mapping the students table

    Inherits from Base
    The table has 3 columns: id, name and grade
    """

    # class variables
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    grade = Column(Integer)
