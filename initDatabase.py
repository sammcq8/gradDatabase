import sqlite3

conn = sqlite3.connect('GradDatabase.db')
c  = conn.cursor()

c.execute(""" CREATE TABLE tblStudents(
                StudentID INTEGER NOT NULL PRIMARY KEY,
                FName TEXT,
                LName TEXT,
                GradYear INTEGER,
                Gender INTEGER,
                Graduating INTEGER DEFAULT 1,
                Walking INTEGER DEFAULT 1,
                Val INTEGER DEFAULT 0,
                Sal INTEGER DEFAULT 0,
                HallOfFame INTEGER DEFAULT 0,
                NHS INTEGER DEFAULT 0,
                HonorsDiploma INTEGER DEFAULT 0,
                HonorsScholar INTEGER DEFAULT 0)
            """)#Boolean Values are stored as integers, 0=false 1=true, Gender, 0 = male, 1 = female
