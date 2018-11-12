import main
import tkinter as tk

class EditStudentsWindowNEW():
    def __init__(self, StudentID):
        top = tk.Toplevel()
        activeStudent = main.returnStudentSID(StudentID)

        top.title("Edit Student")
        top.resizable(width=False, height=False)
        gender = 2
        #Frames
        workspaceFrame = tk.Frame(top, width = 650, height = 500,  padx = 30)

        #Worksace Frame Items


        #variables
        eFNameVariable = tk.StringVar(top, activeStudent[1])
        eLNameVariable = tk.StringVar(top, activeStudent[2])
        eSIDVariable = tk.IntVar(top, activeStudent[0])
        rdbGenderVar = activeStudent[3]
        chkbGraduatingVar = tk.IntVar(top, activeStudent[4])
        chkbWalkingVar = tk.IntVar(top, activeStudent[5])
        chkbSalVar = tk.IntVar(top, activeStudent[7])
        chkbValVar = tk.IntVar(top, activeStudent[6])
        chkbHallOfFameVar = tk.IntVar(top, activeStudent[8])
        chkbNHSVar = tk.IntVar(top, activeStudent[9])
        chkbHonorsScholarVar = tk.IntVar(top, activeStudent[11])
        chkbHonorsDiplomaVar = tk.IntVar(top, activeStudent[10])

        print(chkbWalkingVar.get())
        print(chkbGraduatingVar.get())
        print(chkbSalVar.get())
        print(chkbValVar.get())
        print(chkbHallOfFameVar.get())
        print(chkbNHSVar.get())
        print(chkbHonorsScholarVar.get())
        print(chkbHonorsDiplomaVar.get())

        #Lables
        lblFName = tk.Label(workspaceFrame, text="First Name:  ")
        lblLName = tk.Label(workspaceFrame, text="Last Name:  ")
        lblTitle = tk.Label(workspaceFrame, text = "Marion L Steele High School Graduation Database", pady = 7, anchor = "n")
        lblSID = tk.Label(workspaceFrame, text="Student ID:  ")
        lblGender = tk.Label(workspaceFrame, text="Gender:  ")

        #Entry boxes
        eLName = tk.Entry(workspaceFrame, textvariable = eLNameVariable )
        eFName = tk.Entry(workspaceFrame, textvariable = eFNameVariable )
        eSID = tk.Entry(workspaceFrame, textvariable = eSIDVariable )

        #Radio Buttons
        rdbFemale = tk.Radiobutton(workspaceFrame, text = "Female", variable = rdbGenderVar, value = 1)
        rdbMale = tk.Radiobutton(workspaceFrame, text = "Male", variable = rdbGenderVar, value = 0)

        btnSave = tk.Button(workspaceFrame,
                        text = "Save",
                        command = lambda: chkbHonorsDiplomaVar.get)



                       #checkboxes
        chkbGraduating    = tk.Checkbutton(workspaceFrame, text = "Graduating",     variable = chkbGraduatingVar,    offvalue = 0, onvalue = 1)
        chkbWalking       = tk.Checkbutton(workspaceFrame, text = "Walking",        variable = chkbWalkingVar,       offvalue = 0, onvalue = 1)
        chkbSal           = tk.Checkbutton(workspaceFrame, text = "Salutorian",     variable = chkbSalVar,           offvalue = 0, onvalue = 1)
        chkbVal           = tk.Checkbutton(workspaceFrame, text = "Valedictorian",  variable = chkbValVar,           offvalue = 0, onvalue = 1)
        chkbHallOfFame    = tk.Checkbutton(workspaceFrame, text = "Hall of Fame",   variable = chkbHallOfFameVar,    offvalue = 0, onvalue = 1)
        chkbNHS           = tk.Checkbutton(workspaceFrame, text = "NHS",            variable = chkbNHSVar,           offvalue = 0, onvalue = 1)
        chkbHonorsScholar = tk.Checkbutton(workspaceFrame, text = "Honors Scholar", variable = chkbHonorsScholarVar, offvalue = 0, onvalue = 1)
        chkbHonorsDiploma = tk.Checkbutton(workspaceFrame, text = "Honors Diploma", variable = chkbHonorsDiplomaVar, offvalue = 0, onvalue = 1)

        print(chkbWalkingVar.get())

        #layouts in workspace frame
        workspaceFrame.grid(column = 1, row = 0, sticky = "N")
        lblTitle.grid(row = 0, columnspan = 5)
        lblFName.grid(row = 1)
        eFName.grid(row = 1, column = 1)
        lblLName.grid(row = 2)
        eLName.grid(row = 2, column = 1)
        lblSID.grid(row = 3)
        eSID.grid(row = 3, column = 1)

        lblGender.grid(row = 4)
        rdbFemale.grid(row = 4, column = 2)
        rdbMale.grid(row = 4, column = 1)

        chkbGraduating.grid(row = 6, column = 1)
        chkbWalking.grid(row = 6, column = 2)
        chkbSal.grid(row = 7, column = 1)
        chkbVal.grid(row = 7, column = 2)
        chkbHallOfFame.grid(row = 8, column = 1)
        chkbNHS.grid(row = 8, column = 2)
        chkbHonorsDiploma.grid(row = 9, column = 1)
        chkbHonorsScholar.grid(row = 9, column = 2)

        btnSave.grid(row = 10, column = 2)



        tup = ("Natalie", "Knight", 111111)
        self.populate(tup)
    def populate(self, studentName ):
            student = main.returnStudent(studentName)
            print(student)
            #eSID.set(student[0])
            #eFName.set(student[2])
            #eLname.insert(0,studentName[1])
