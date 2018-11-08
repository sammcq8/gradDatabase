import sqlite3
import csv as csv

#Connect to the database
conn = sqlite3.connect('GradDatabase.db')
c  = conn.cursor()


def searchStudents(SID, Fname, Lname):
    if(SID == ""):
        SID = None
    if(Fname == ""):
        Fname = None
    if(Lname == ""):
        Lname = None
    c.execute("""
        SELECT fname, lname, StudentID
        FROM tblStudents
        WHERE LName = CASE WHEN :LName IS NULL THEN LName ELSE :LName END
        AND FName = CASE WHEN :FName IS NULL THEN FName ELSE :FName END
        AND StudentID = CASE WHEN :SID IS NULL THEN StudentID ELSE :SID END""",
        {'LName': Lname, 'FName' : Fname, 'SID' : SID })
    return c.fetchall()

print(searchStudents(None, "Sean", None))

def returnStudent(studentInfo):
    Fname = studentInfo[0]
    Lname = studentInfo[1]
    SID = studentInfo[2]
    c.execute("""
        SELECT StudentID, FName, LName, Gender, Graduating, Walking, Val, Sal, HallOfFame, NHS, HonorsDiploma, HonorsScholar
        FROM tblStudents
        WHERE LName = :LName
        AND FName = :FName
        AND StudentID = :SID """,
        {'LName': Lname, 'FName' : Fname, 'SID' : SID })
    return c.fetchone()

def returnStudentSID(SID):
    c.execute("""
        SELECT StudentID, FName, LName, Gender, Graduating, Walking, Val, Sal, HallOfFame, NHS, HonorsDiploma, HonorsScholar
        FROM tblStudents
        WHERE StudentID = :SID """,
        {'SID' : SID })
    return c.fetchone()

def createStudent(SID, FName, LName, GradYear, Gender):
    if (Gender == "Male"):
        genderNum = 0
    else:
        genderNum = 1
    #For gender, 0 = Male 1=Female
    c.execute("""INSERT INTO tblStudents (StudentID, FName, LName, GradYear, Gender)
                    VALUES ( :SID, :FName, :LName, :GradYear, :Gender)
                """, {'SID' : SID, 'FName' : FName, 'LName' : LName, 'GradYear' : GradYear, 'Gender' : genderNum})


def importCsvParser(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            StudentID = row[0]
            FName = row[1]
            LName = row[2]
            GradYear = row[3]
            Gender = row[4]
            createStudent(StudentID, FName, LName, GradYear, Gender)
            line_count = line_count + 1
        conn.commit()
        print(f'Processed {line_count} lines.')
student = 111111
def populate():
    print(student)

    eSIDVar.set(student[0])
    eFNameVar.set(student[2])
    eLNameVar.set(student[1])

#def populate():

#importCsvParser('csvFunzies.csv')

#c.execute("SELECT * FROM tblStudents")
#print (c.fetchall())
