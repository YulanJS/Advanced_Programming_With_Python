import sqlite3
from sqlalchemy import create_engine, select
from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

connection = sqlite3.connect('cs122a.db')
# cursor, interface to sql database
cursor = connection.cursor()
# create a table in database
cursor.execute("""CREATE TABLE students
(id integer primary key, name text, grade integer)""")
cursor.execute("""INSERT INTO students values(10, 'Alex', 100)""")
# ? as place holders; system will auto increase to create id for rows
cursor.execute("""INSERT INTO students (name, grade) VALUES(?, ?)""",
               ("Zoe", 95))
curr_name = "Andrew"
curr_grade = 90
cursor.execute("""INSERT INTO students (name, grade) VALUES(?, ?)""",
               (curr_name, curr_grade))
# If using f strings and {variable}, it is insecure. It can work, but
# we should never use this way.
# It makes the program vulnerable to an SQL injection attack.

# student and finalgrade are keys of the dictionary that contains a row
cursor.execute("""INSERT INTO students(name, grade) VALUES(:student, 
:finalgrade)""", {"student": 'Andrea', "finalgrade": 99})
connection.commit()
connection.close()

# after closing the connection, we get an error
# result = cursor.execute("SELECT * FROM students")

# build a new connection
connection = sqlite3.connect("cs122a.db")
cursor = connection.cursor()
result = cursor.execute("SELECT * FROM students")
print(result)  # get Cursor object
print(result.fetchall())  # get a list of tuples
# [(10, 'Alex', 100), (11, 'Zoe', 95), (12, 'Andrew', 90),
# (13, 'Andrea', 99)]
print(result.fetchall())  # fetchall() again will get an empty list

# using like here
# place holder correspond to values contained in a tuple, even if it
# is a single value -> make a tuple
result = cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('zoe', ))
print(result.fetchone())  # get a tuple for Zoe
print(result.fetchone())  # get None because next one does not exist

result = cursor.execute("SELECT * FROM students WHERE grade >= ?", (95,))
print(result.fetchone())
print(result.fetchone())  # get another entry
print(result.fetchone())
# after getting results one by one, getting None in the end

result = cursor.execute("SELECT * FROM students WHERE grade != ?", (100, ))
print(result.fetchmany(2))
# [(11, 'Zoe', 95), (12, 'Andrew', 90)]
print(result.fetchmany(2))
# [(13, 'Andrea', 99)]

# update a row
cursor.execute("""UPDATE students SET GRADE=? WHERE name=?""", (100, "Andrea"))
# <sqlite3.Cursor object at 0x00000189A1EC6C00>
result = cursor.execute("SELECT * FROM students")
for each_student in result:
    print(each_student)
"""
(10, 'Alex', 100)
(11, 'Zoe', 95)
(12, 'Andrew', 90)
(13, 'Andrea', 100)
"""
# must commit to save the changed result into database
connection.commit()
connection.close()

# change better: using ORM(Object Relational Mapper)
# maps a row into a python object, ORM, a software, will work for us
# Django, SQLAlchemy... ORM software
# We learn SQLAlchemy now.
# It will translate python code into SQL statements. (Core)
# ORM Engine:
# import ......
engine = create_engine('sqlite:///cs122b.db')
metadata = MetaData(engine)  # MetaData object
students = Table('students', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String),
                 Column('grade', Integer))
Session = sessionmaker(bind=engine)  # it returns a class
session = Session()
metadata.create_all(engine)  # table created
ins = students.insert().values(id=10, name='Alex', grade=100)
print(ins)  # SQL command generated for us
# INSERT INTO students (id, name, grade) VALUES (?, ?, ?)
session.execute(ins)
# <sqlalchemy.engine.result.ResultProxy object at 0x00000189A2C183C8>
session.commit()
result = session.execute(select([students]))
print(result)
for each_row in result:
    print(each_row)
"""
<sqlalchemy.engine.result.ResultProxy object at 0x00000189A2C166A0>
(10, 'Alex', 100)
"""

# update c means col
result = session.execute(students.update().values(grade=99).where(
    students.c.name == 'Alex'))

# mapping a table to a class
# import from lecture26.py class definitions
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


new_student = Student(name='zoe', grade=90)
session.add(new_student)
session.commit()
# student class
result = session.query(Student).all()
# type of result: a_list_of_Student_object
