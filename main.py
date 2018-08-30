import sqlite3
from students import Student

#Connect to the database
conn = sqlite3.connect('database.db')
c  = conn.cursor()



def searchByColor(searchTerm):
    c.execute("""SELECT fname, lname
                FROM StudentColors
                WHERE color Like :color""", {'color' : searchTerm+'%'}     )
    print(c.fetchall())

def returnStudent(searchTerm):
    c.execute("""SELECT fname, lname
                FROM StudentColors
                WHERE lname Like :lname""", {'lname': searchTerm})
    print(c.fetchall())

#returnStudent("McQuate", "Last Name")
