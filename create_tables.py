import sqlite3 

#Connect to db
conn=sqlite3.connect('StudentInfo.db')

#create cursor
c=conn.cursor()

#create tables

c.execute("""
CREATE TABLE IF NOT EXISTS user(
    userID VARCHAR(12) PRIMARY KEY,
    uPass VARCHAR(100) NOT NULL,
    isStudent BOOL DEFAULT FALSE,
    isTeacher BOOL DEFAULT FALSE 
) 
""") 

c.execute("""
CREATE TABLE IF NOT EXISTS student(
    studentID VARCHAR(12) PRIMARY KEY,
    email VARCHAR(50) NOT NULL,
    name VARCHAR(50) NOT NULL,
    gender VARCHAR(2) NOT NULL,
    fatherName VARCHAR(50) NOT NULL,
    motherName VARCHAR(50) NOT NULL,
    address VARCHAR(200) NOT NULL,
    cell VARCHAR(20),
    deptID int NOT NULL,
    batch int NOT NULL,
    FOREIGN KEY(deptID) REFERENCES department(deptID)
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS department(
    deptID INTEGER PRIMARY KEY AUTOINCREMENT,
    dName VARCHAR(50) NOT NULL
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS course(
    courseCode VARCHAR(10) PRIMARY KEY,
    courseTitle VARCHAR(50) NOT NULL,
    courseCredit int NOT NULL
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS registeredCourse(
    studentID VARCHAR(12),
    courseCode VARCHAR(10),
    semester VARCHAR(20) NOT NULL,
    section VARCHAR(3) NOT NULL,
    teacherID VARCHAR(12) NOT NULL,
    FOREIGN KEY(teacherID) REFERENCES teacher(teacherID),
    PRIMARY KEY(studentID,courseCode)
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS result(
    studentID VARCHAR(12),
    courseCode VARCHAR(10),
    semester VARCHAR(20) NOT NULL,
    grade DOUBLE(4,2) NOT NULL,
    PRIMARY KEY(studentID,courseCode,semester)
)
""")


c.execute("""
CREATE TABLE IF NOT EXISTS teacher(
    teacherID VARCHAR(12) PRIMARY KEY,
    tEmail VARCHAR(50) NOT NULL,
    tName VARCHAR(50) NOT NULL,
    tInitial VARCHAR(10) NOT NULL,
    designation VARCHAR(50) NOT NULL,
    deptID int NOT NULL,
    cell VARCHAR(20) NOT NULL,
    FOREIGN KEY(deptID) REFERENCES department(deptID)
)
""")


c.execute("""
CREATE TABLE IF NOT EXISTS library(
    studentID VARCHAR(12),
    bookID VARCHAR(50),
    Taken DATE,
    Return DATE,
    FOREIGN KEY(studentID) REFERENCES student(studentID),
    FOREIGN KEY(bookID) REFERENCES book(bookID)
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS book(
    bookID VARCHAR(12) PRIMARY KEY,
    bName VARCHAR(100) NOT NULL,
    bcategory VARCHAR(50) NOT NULL
)
""")


conn.commit()