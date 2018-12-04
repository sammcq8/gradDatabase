import tkinter as tk
from tkinter import filedialog
import sqlite3
import main
import reports
import NewEditStudents


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

        #Frames
        menuFrame = tk.Frame(self, width = 150, height = 500, bg = "grey", padx = 10)
        workspaceFrame = tk.Frame(self, width = 650, height = 500,  padx = 30)


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
        workspaceFrame.grid(column = 1, row = 0)
        btnMenu.grid(column = 0, row = 0)
        btnImportStudents.grid(row = 2)
        btnEditStudents.grid(row = 3)
        btnMassEditStudents.grid(row = 4)
        btnRunReports.grid(row = 5)



        btnShow.grid(row = 10, column = 2)
        btnQuit.grid(row = 11, column = 2, sticky = "S")
        btnSearch.grid(row = 12, column = 2)




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

        btnImport = tk.Button(workspaceFrame, text = "Import Students",pady = 15, command = lambda: main.importCsvParser("students.csv"))
        #________________________LAYOUTS__________________________________________
        workspaceFrame.grid(column = 1, row = 0)
        lblTitle.grid(column = 0, row = 0)
        btnImport.grid(column = 0, row = 1)

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
        workspaceFrame = tk.Frame(self, width = 650, height = 500,  padx = 30)

        #Workspace Frame Items
        #filepath = (filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*"))))
        #BUttons
        HonorsScholar = tk.Button(workspaceFrame, text = "Honors Scholar", pady = 5, padx = 5, command = reports.HonorScholarList)
        WalkingOrder = tk.Button(workspaceFrame, text = "Boy Girl Walking Order", pady = 5, padx = 5, command = reports.boyGirlWalkingOrder)
        HonorsDiploma = tk.Button(workspaceFrame, text = "Honors Diploma", pady = 5, padx = 5, command = reports.HonorsDiplomaList)
        Graduating = tk.Button(workspaceFrame, text = "Graduating", pady = 5, padx = 5, command =  lambda: reports.Graduating((filedialog.asksaveasfile(initialdir = "/",title = "Save As...", defaultextension = ".docx"))))

        #buttons
        btnMenu = tk.Button(menuFrame, text = "Menu", pady = 15, command = lambda: controller.showFrame(MenuWindow))
        btnImportStudents = tk.Button(menuFrame, text = "Import Students",pady = 15,command = lambda: controller.showFrame(ImportStudentsWindow))
        btnEditStudents = tk.Button(menuFrame, text = "Edit Students",pady = 15,command = lambda: controller.showFrame(EditStudentsWindow))
        btnMassEditStudents = tk.Button(menuFrame, text = "Mass Edit Students",pady = 15,command = lambda: controller.showFrame(MassEditStudentsWindow))
        btnRunReports = tk.Button(menuFrame, text = "Run Reports",pady = 15,command = lambda: controller.showFrame(RunReportsWindow))



        lblTitle = tk.Label(workspaceFrame, text = "Marion L Steele High School Graduation Database - Run Reports", pady = 7, anchor = "n")

        #________________________LAYOUTS__________________________________________
        workspaceFrame.grid(column = 1, row = 1)
        lblTitle.grid(column = 0, row = 0, columnspan = 2)

        WalkingOrder.grid(column = 1, row = 1)
        HonorsScholar.grid(column = 0, row = 1)
        HonorsDiploma.grid(column = 1, row = 2)
        Graduating.grid(column = 0, row = 2)
        #layouts in menu frame
        menuFrame.grid(column = 0, row = 1)

        btnMenu.grid(column = 0, row = 0)
        btnImportStudents.grid(row = 2)
        btnEditStudents.grid(row = 3)
        btnMassEditStudents.grid(row = 4)
        btnRunReports.grid(row = 5)

        #workspace


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
        activeStudent = list.get("active")
        #print(activeStudent)
        NewEditStudents.EditStudentsWindowNEW(activeStudent[2])
        top.destroy()
        #self.destroy()







root = GradDatabase()
root.mainloop()
