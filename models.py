from app import db

from sqlalchemy import (
create_engine,
Column,
Integer,
String,
ForeignKey,
)

from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://vadim:12345@localhost/lessons?charset=utf8mb4', echo=True)
db.session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db.session.query_property()

class Class(Base):
    __tablename__ = "Class"
    idclass = Column(Integer, primary_key=True)
    name = Column(String(15))

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return "<Class {}>".format(self.name)


class Subject(Base):
    __tablename__ = "Subject"
    idsubject = Column(Integer, primary_key=True)
    name = Column(String(20))

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return "<Subject {}>".format(self.name)


class Teacher(Base):
    __tablename__ = "Teacher"
    idteacher = Column(Integer, primary_key=True)
    fullname = Column(String(20))
    qualification = Column(String(20))

    def __init__(self, fullname=None, qualification=None):
        self.fullname = fullname
        self.qualification = qualification

    def __repr__(self):
        return "<Teacher {}>".format(self.name)


class Learningactivities(Base):
    __tablename__ = "Learningactivities"
    idclass = Column(Integer, ForeignKey("Class.idclass"), primary_key=True)
    Class = relationship("Class")
    idteacher = Column(Integer, ForeignKey("Teacher.idteacher"), primary_key=True)
    Teacher = relationship("Teacher")
    idsubject = Column(Integer, ForeignKey("Subject.idsubject"), primary_key=True)
    Subject = relationship("Subject")

    def __init__(self, Class=None, Teacher=None, Subject=None):
        self.Class = Class
        self.Teacher = Teacher
        self.Subject = Subject


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    print("Database created")