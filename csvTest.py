import csv
import sqlite3
from main import createStudent
conn = sqlite3.connect('GradDatabase.db')
c  = conn.cursor()


def csvParser(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            StudentID = row[0].strip()
            FName = row[1].strip()
            LName = row[2].strip()
            GradYear = row[3].strip()
            Gender = row[4].strip()
            createStudent(StudentID, FName, LName, GradYear, Gender)
            line_count += 1
            conn.commit()
        print(f'Processed {line_count} lines.')


csvParser('csvFunzies.csv')
