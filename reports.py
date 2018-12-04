import sqlite3
import csv as csv
import itertools
import docx

#Connect to the database
conn = sqlite3.connect('GradDatabase.db')
c  = conn.cursor()


def HonorScholarList():
    c.execute("""
        SELECT Fname, Lname FROM tblStudents
        WHERE HonorsScholar = 1
        ORDER BY LOWER(Lname) ASC""")

    print(c.fetchall())

def boyGirlWalkingOrder():
    c.execute("""
        SELECT Fname, Lname FROM tblStudents
        WHERE gender = 1
        AND Walking = 1
        AND Graduating = 1
        ORDER BY LOWER(Lname) ASC""")

    girls = c.fetchall()
    c.execute("""
        SELECT Fname, Lname FROM tblStudents
        WHERE gender = 0
        AND Walking = 1
        AND Graduating = 1
        ORDER BY LOWER(Lname) ASC""")
    boys = c.fetchall()
    print("Boys -")
    print(boys)
    print("Girls -")
    print(girls)

    for boy, girl in itertools.zip_longest( boys, girls):
        if boy is not None:
            document.add_paragraph(boy[0] + " " + boy[1], style = "Normal")
        if girl is not None:
            document.add_paragraph(girl[0] + " " + girl[1], style = "Normal")
    document.save(filepath)


def HonorsDiplomaList():
    c.execute("""
        SELECT Fname, Lname FROM tblStudents
        WHERE HonorsDiploma = 1
        ORDER BY LOWER(Lname) ASC""")
    document = docx.Document("ReportTemplates/GraduatingAlphabetical.docx")

    for item in c.fetchall():
        document.add_paragraph(item[0] + " " + item[1], style = "Normal")
        print(item)
    document.save(filepath)
    print(filepath)

def Graduating(filepath):
    c.execute("""
        SELECT Fname, Lname FROM tblStudents
        WHERE Graduating = 1
        ORDER BY LOWER(Lname) ASC""")
    document = docx.Document("ReportTemplates/GraduatingAlphabetical.docx")

    for item in c.fetchall():
        document.add_paragraph(item[0] + " " + item[1], style = "Normal")
        print(item)
    document.save(filepath)
