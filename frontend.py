import tkinter as tk
import sqlite3
import main


activeStudent = main.returnStudentSID(111111)
#Main section of the GUI program
class GradDatabase(tk.Tk):

    #Establishes the window for the program, every frame of the window has it's own entry into a dictionary
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, *kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        ESframe = EditStudentsWindow(container, self)
        MenuFrame = MenuWindow(container, self)
        ISFrame = ImportStudentsWindow(container, self)
        MESFrame = MassEditStudentsWindow(container, self)
        RRFrame = RunReportsWindow(container, self)

        self.frames[EditStudentsWindow] = ESframe
        self.frames[MenuWindow] = MenuFrame
        self.frames[ImportStudentsWindow] = ISFrame
        self.frames[MassEditStudentsWindow] = MESFrame
        self.frames[RunReportsWindow] = RRFrame

        ESframe.grid(row=0,column=0,sticky="nsew")
        MenuFrame.grid(row=0,column=0,sticky="nsew")
        ISFrame.grid(row=0,column=0,sticky="nsew")
        MESFrame.grid(row=0,column=0,sticky="nsew")
        RRFrame.grid(row=0,column=0,sticky="nsew")

        self.showFrame(MenuWindow)
    #Takes and argument (cont) that is the frame needed, refrences the dictionary and makes that frame the toplevel
    def showFrame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class EditStudentsWindow(tk.Frame):
    gender = 2

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        #root = tk.Tk()
        #root.title("Graduation Database")
        #root.resizable(width=False, height=False)
        gender = 2
        #Frames
        menuFrame = tk.Frame(self, width = 150, height = 500, bg = "grey", padx = 10)
        workspaceFrame = tk.Frame(self, width = 650, height = 500,  padx = 30)

        #Worksace Frame Items
        global activeStudent
        eFNameVariable = tk.StringVar(self, activeStudent[1])
        eLNameVariable = tk.StringVar(self, activeStudent[2])
        eSIDVariable = tk.IntVar(self, activeStudent[0])
        print(eFNameVariable)


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
        rdbFemale = tk.Radiobutton(workspaceFrame, text = "Female", variable = gender, value = 1)
        rdbMale = tk.Radiobutton(workspaceFrame, text = "Male", variable = gender, value = 0)

        #buttons
        btnQuit = tk.Button(workspaceFrame,
                       text="Quit",
                       fg="red",
                       command=quit)

        btnShow = tk.Button(workspaceFrame,
                        text = "Show",
                        #command = lambda: returnStudent(eLName.get())
                        )
        #top = SearchBox(self)
        btnSearch = tk.Button(workspaceFrame,
                       text="Search",
                       command= lambda : SearchBox(self))

                       #checkboxes
        chkbGraduating = tk.Checkbutton(workspaceFrame, text = "Graduating")
        chkbWalking = tk.Checkbutton(workspaceFrame, text = "Walking")
        chkbSal = tk.Checkbutton(workspaceFrame, text = "Salutorian")
        chkbVal = tk.Checkbutton(workspaceFrame, text = "Valedictorian")
        chkbHallOfFame = tk.Checkbutton(workspaceFrame, text = "Hall of Fame")
        chkbNHS = tk.Checkbutton(workspaceFrame, text = "NHS")

        #Menu Frames

        #labels


        #buttons
        btnMenu = tk.Button(menuFrame, text = "Menu", pady = 15, command = lambda: controller.showFrame(MenuWindow))
        btnImportStudents = tk.Button(menuFrame, text = "Import Students",pady = 15, command = lambda: controller.showFrame(ImportStudentsWindow))
        btnEditStudents = tk.Button(menuFrame, text = "Edit Students",pady = 15,command = lambda: controller.showFrame(EditStudentsWindow))
        btnMassEditStudents = tk.Button(menuFrame, text = "Mass Edit Students",pady = 15,command = lambda: controller.showFrame(MassEditStudentsWindow))
        btnRunReports = tk.Button(menuFrame, text = "Run Reports",pady = 15,command = lambda: controller.showFrame(RunReportsWindow))



                    #layouts in menu frame
        menuFrame.grid(column = 0, row = 0)

        btnMenu.grid(column = 0, row = 0)
        btnImportStudents.grid(row = 2)
        btnEditStudents.grid(row = 3)
        btnMassEditStudents.grid(row = 4)
        btnRunReports.grid(row = 5)

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

        btnShow.grid(row = 10, column = 2)
        btnQuit.grid(row = 11, column = 2, sticky = "S")
        btnSearch.grid(row = 12, column = 2)


        tup = ("Natalie", "Knight", 111111)
        self.populate(tup)
    def populate(self, studentName ):
            student = main.returnStudent(studentName)
            print(student)
            #eSID.set(student[0])
            #eFName.set(student[2])
            #eLname.insert(0,studentName[1])




#    def save(self):


class MenuWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        #labels


        #buttons
        btnMenu = tk.Button(self, text = "Menu", padx = 50, pady = 15, anchor = "w", command = lambda: controller.showFrame(MenuWindow))
        btnImportStudents = tk.Button(self, text = "Import Students", padx = 50, pady = 15,command = lambda: controller.showFrame(ImportStudentsWindow))
        btnEditStudents = tk.Button(self, text = "Edit Students", padx = 50, pady = 15, command = lambda: controller.showFrame(EditStudentsWindow))
        btnMassEditStudents = tk.Button(self, text = "Mass Edit Students", padx = 50, pady = 15, command = lambda: controller.showFrame(MassEditStudentsWindow))
        btnRunReports = tk.Button(self, text = "Run Reports", padx = 50, pady = 15, command = lambda: controller.showFrame(RunReportsWindow))

        #________________________LAYOUTS__________________________________________


        btnMenu.pack()
        btnImportStudents.pack()
        btnEditStudents.pack()
        btnMassEditStudents.pack()
        btnRunReports.pack()

class ImportStudentsWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuFrame = tk.Frame(self, width = 150, height = 500, bg = "grey", padx = 10)

        #buttons
        btnMenu = tk.Button(menuFrame, text = "Menu", pady = 15, command = lambda: controller.showFrame(MenuWindow))
        btnImportStudents = tk.Button(menuFrame, text = "Import Students",pady = 15,command = lambda: controller.showFrame(ImportStudentsWindow))
        btnEditStudents = tk.Button(menuFrame, text = "Edit Students",pady = 15,command = lambda: controller.showFrame(EditStudentsWindow))
        btnMassEditStudents = tk.Button(menuFrame, text = "Mass Edit Students",pady = 15, command = lambda: controller.showFrame(MassEditStudentsWindow))
        btnRunReports = tk.Button(menuFrame, text = "Run Reports",pady = 15, command = lambda: controller.showFrame(RunReportsWindow))



        #layouts in menu frame
        menuFrame.grid(column = 0, row = 0)

        btnMenu.grid(column = 0, row = 0)
        btnImportStudents.grid(row = 2)
        btnEditStudents.grid(row = 3)
        btnMassEditStudents.grid(row = 4)
        btnRunReports.grid(row = 5)

        #workspace

        workspaceFrame = tk.Frame(self, width = 650, height = 500,  padx = 30)

        lblTitle = tk.Label(workspaceFrame, text = "Marion L Steele High School Graduation Database - Import Students", pady = 7, anchor = "n")

        #________________________LAYOUTS__________________________________________
        workspaceFrame.grid(column = 1, row = 0)
        lblTitle.grid(column = 0, row = 0)

class MassEditStudentsWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuFrame = tk.Frame(self, width = 150, height = 500, bg = "grey", padx = 10)

        #buttons
        btnMenu = tk.Button(menuFrame, text = "Menu", pady = 15, command = lambda: controller.showFrame(MenuWindow))
        btnImportStudents = tk.Button(menuFrame, text = "Import Students",pady = 15,command = lambda: controller.showFrame(ImportStudentsWindow))
        btnEditStudents = tk.Button(menuFrame, text = "Edit Students",pady = 15,command = lambda: controller.showFrame(EditStudentsWindow))
        btnMassEditStudents = tk.Button(menuFrame, text = "Mass Edit Students",pady = 15,command = lambda: controller.showFrame(MassEditStudentsWindow))
        btnRunReports = tk.Button(menuFrame, text = "Run Reports",pady = 15,command = lambda: controller.showFrame(RunReportsWindow))



        #layouts in menu frame
        menuFrame.grid(column = 0, row = 0)

        btnMenu.grid(column = 0, row = 0)
        btnImportStudents.grid(row = 2)
        btnEditStudents.grid(row = 3)
        btnMassEditStudents.grid(row = 4)
        btnRunReports.grid(row = 5)

        #workspace

        workspaceFrame = tk.Frame(self, width = 650, height = 500,  padx = 30)

        lblTitle = tk.Label(workspaceFrame, text = "Marion L Steele High School Graduation Database - Mass Edit Students", pady = 7, anchor = "n")

        #________________________LAYOUTS__________________________________________
        workspaceFrame.grid(column = 1, row = 0)
        lblTitle.grid(column = 0, row = 0)

class RunReportsWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuFrame = tk.Frame(self, width = 150, height = 500, bg = "grey", padx = 10)

        #buttons
        btnMenu = tk.Button(menuFrame, text = "Menu", pady = 15, command = lambda: controller.showFrame(MenuWindow))
        btnImportStudents = tk.Button(menuFrame, text = "Import Students",pady = 15,command = lambda: controller.showFrame(ImportStudentsWindow))
        btnEditStudents = tk.Button(menuFrame, text = "Edit Students",pady = 15,command = lambda: controller.showFrame(EditStudentsWindow))
        btnMassEditStudents = tk.Button(menuFrame, text = "Mass Edit Students",pady = 15,command = lambda: controller.showFrame(MassEditStudentsWindow))
        btnRunReports = tk.Button(menuFrame, text = "Run Reports",pady = 15,command = lambda: controller.showFrame(RunReportsWindow))



        #layouts in menu frame
        menuFrame.grid(column = 0, row = 0)

        btnMenu.grid(column = 0, row = 0)
        btnImportStudents.grid(row = 2)
        btnEditStudents.grid(row = 3)
        btnMassEditStudents.grid(row = 4)
        btnRunReports.grid(row = 5)

        #workspace

        workspaceFrame = tk.Frame(self, width = 650, height = 500,  padx = 30)

        lblTitle = tk.Label(workspaceFrame, text = "Marion L Steele High School Graduation Database - Run Reports", pady = 7, anchor = "n")

        #________________________LAYOUTS__________________________________________
        workspaceFrame.grid(column = 1, row = 0)
        lblTitle.grid(column = 0, row = 0)

class SearchBox():


    def __init__(self, parent):
        top = tk.Toplevel()
        top.title("Search...")
        SearchTitle = tk.Label(top, text = "Enter Student Information to Search", padx = 5, pady = 5)
        SID = tk.Label(top, text = "Student ID:", padx = 5, pady = 5)
        FName = tk.Label(top, text = "First Name:", padx = 5, pady = 5)
        LName = tk.Label(top, text = "Last Name:", padx = 5, pady = 5)

        ESID = tk.Entry(top)
        EFName = tk.Entry(top)
        ELName = tk.Entry(top)

        btnSearch = tk.Button(top, text = "Search", anchor = "sw", command = lambda: self.search(top, ESID, EFName, ELName)  )

        SearchTitle.grid(row = 1, column = 1, columnspan = 2)
        SID.grid(row = 2, column = 1,)
        FName.grid(row = 3, column = 1,)
        LName.grid(row = 4, column = 1,)

        ESID.grid(row = 2, column = 2)
        EFName.grid(row = 3, column = 2)
        ELName.grid(row = 4, column = 2)
        btnSearch.grid(row = 5, column = 3)

    def search(self, top, ESID, EFName, ELName):
        SearchResults(self, main.searchStudents(ESID.get(), EFName.get(), ELName.get()))
        top.destroy()

class SearchResults():

    def __init__(self, parent, results ):
        top = tk.Toplevel()


        top.title("Results")
        title = tk.Label(top, text = "Select one:", pady = 10)
        title.pack()

        lbresults = tk.Listbox(top, width = 50)
        for student in results:
            lbresults.insert("end", student)
        lbresults.pack()

        btnEnter = tk.Button(top, text = "Enter", command = lambda: self.enter(self, lbresults, top) )
        btnEnter.pack()

    def enter(self, parent, list, top):
        global activeStudent
        activeStudent = list.get("active")
        #print(activeStudent)
        #main.populate(activeStudent)
        top.destroy()







root = GradDatabase()
root.mainloop()
