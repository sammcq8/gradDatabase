import functions
import tkinter as tk

class EditStudentsWindowNEW():

    def __init__(self, StudentID):
        top = tk.Toplevel()
        activeStudent = functions.returnStudentSID(StudentID)

        top.title("Edit Student")
        top.iconbitmap(r"Files\CometLogo.ico")
        top.resizable(width=False, height=False)
        #Frames
        workspaceFrame = tk.Frame(top, width = 650, height = 500,  padx = 30)
        #Worksace Frame Items


        #variables
        eFNameVar = tk.StringVar(top, activeStudent[1])
        eMNameVar = tk.StringVar(top, activeStudent[12])
        eLNameVar = tk.StringVar(top, activeStudent[2])
        eSIDVar = tk.IntVar(top, activeStudent[0])
        rdbGenderVar = tk.IntVar(top, activeStudent[3])
        chkbGraduatingVar = tk.IntVar(workspaceFrame, activeStudent[4])
        chkbWalkingVar = tk.IntVar(workspaceFrame, activeStudent[5])
        chkbSalVar = tk.IntVar(top, activeStudent[7])
        chkbValVar = tk.IntVar(top, activeStudent[6])
        chkbHallOfFameVar = tk.IntVar(top, activeStudent[8])
        chkbNHSVar = tk.IntVar(top, activeStudent[9])
        chkbHonorsScholarVar = tk.IntVar(top, activeStudent[11])
        chkbHonorsDiplomaVar = tk.IntVar(top, activeStudent[10])


        #Lables
        lblFName = tk.Label(workspaceFrame, text="First Name:  ")
        lblMName = tk.Label(workspaceFrame, text="Middle Name:  ")
        lblLName = tk.Label(workspaceFrame, text="Last Name:  ")
        lblTitle = tk.Label(workspaceFrame, text = "Marion L Steele High School Graduation Database", pady = 7, anchor = "n")
        lblSID = tk.Label(workspaceFrame, text="Student ID:  ")
        lblGender = tk.Label(workspaceFrame, text="Gender:  ")

        #Entry boxes
        eLName = tk.Entry(workspaceFrame, textvariable = eLNameVar )
        eFName = tk.Entry(workspaceFrame, textvariable = eFNameVar )
        eMName = tk.Entry(workspaceFrame, textvariable = eMNameVar )
        eSID = tk.Entry(workspaceFrame, textvariable = eSIDVar )


        #Radio Buttons
        rdbFemale = tk.Radiobutton(workspaceFrame, text = "Female", variable = rdbGenderVar, value = 1)
        rdbMale = tk.Radiobutton(workspaceFrame, text = "Male", variable = rdbGenderVar, value = 0)

        btnSave = tk.Button(workspaceFrame, text = "Save", command = lambda: functions.updateStudent((eFNameVar.get(), eLNameVar.get(), eSIDVar.get(), rdbGenderVar.get(), chkbGraduatingVar.get(), chkbWalkingVar.get(), chkbSalVar.get(), chkbValVar.get(), chkbHallOfFameVar.get(), chkbNHSVar.get(), chkbHonorsScholarVar.get(), chkbHonorsDiplomaVar.get(), eMNameVar.get()  )))

        #These sad buttons were the only way I got it to work correctly :(
        btnWalking =       tk.Button(workspaceFrame, command = lambda: print(chkbWalkingVar.get()))
        btnGraduating =    tk.Button(workspaceFrame, command = lambda: print(chkbGraduatingVar.get()))
        btnSal =           tk.Button(workspaceFrame, command = lambda: print(chkbSalVar.get()))
        btnVal =           tk.Button(workspaceFrame, command = lambda: print(chkbValVar.get()))
        btnHallOfFame =    tk.Button(workspaceFrame, command = lambda: print(chkbHallOfFameVar.get()))
        btnNHS =           tk.Button(workspaceFrame,  command = lambda: print(chkbNHSVar.get()))
        btnHonorsScholar = tk.Button(workspaceFrame,  command = lambda: print(chkbHonorsScholarVar.get()))
        btnHonorsDiploma = tk.Button(workspaceFrame,  command = lambda: print(chkbHonorsDiplomaVar.get()))


                       #checkboxes
        chkbGraduating    = tk.Checkbutton(workspaceFrame, text = "Graduating",     variable = chkbGraduatingVar,    offvalue = 0, onvalue = 1)
        chkbWalking       = tk.Checkbutton(workspaceFrame, text = "Walking",        variable = chkbWalkingVar,       offvalue = 0, onvalue = 1)
        chkbSal           = tk.Checkbutton(workspaceFrame, text = "Salutorian",     variable = chkbSalVar,           offvalue = 0, onvalue = 1)
        chkbVal           = tk.Checkbutton(workspaceFrame, text = "Valedictorian",  variable = chkbValVar,           offvalue = 0, onvalue = 1)
        chkbHallOfFame    = tk.Checkbutton(workspaceFrame, text = "Hall of Fame",   variable = chkbHallOfFameVar,    offvalue = 0, onvalue = 1)
        chkbNHS           = tk.Checkbutton(workspaceFrame, text = "NHS",            variable = chkbNHSVar,           offvalue = 0, onvalue = 1)
        chkbHonorsScholar = tk.Checkbutton(workspaceFrame, text = "Honors Scholar", variable = chkbHonorsScholarVar, offvalue = 0, onvalue = 1)
        chkbHonorsDiploma = tk.Checkbutton(workspaceFrame, text = "Honors Diploma", variable = chkbHonorsDiplomaVar, offvalue = 0, onvalue = 1)



        chkbGraduating.grid(row = 6, column = 1)
        chkbWalking.grid(row = 6, column = 2)
        chkbSal.grid(row = 7, column = 1)
        chkbVal.grid(row = 7, column = 2)
        chkbHallOfFame.grid(row = 8, column = 1)
        chkbNHS.grid(row = 8, column = 2)
        chkbHonorsDiploma.grid(row = 9, column = 1)
        chkbHonorsScholar.grid(row = 9, column = 2)

        #layouts in workspace frame
        workspaceFrame.grid(column = 1, row = 0, sticky = "N")
        lblTitle.grid(row = 0, columnspan = 5)
        lblFName.grid(row = 1)
        eFName.grid(row = 1, column = 1)
        lblMName.grid(row = 2)
        eMName.grid(row = 2, column = 1)
        lblLName.grid(row = 3)
        eLName.grid(row = 3, column = 1)
        lblSID.grid(row = 4)
        eSID.grid(row = 4, column = 1)

        lblGender.grid(row = 5)
        rdbFemale.grid(row = 5, column = 2)
        rdbMale.grid(row = 5, column = 1)

        btnSave.grid(row = 10, column = 2)
