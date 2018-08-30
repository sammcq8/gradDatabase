import tkinter as tk
from main import returnStudent

root = tk.Tk()

#First Name
lblFName = tk.Label(root, text="First Name").grid(row = 1)
eFName = tk.Entry(root)
eFName.grid(row = 1, column = 1)

#Last Name
lblLName = tk.Label(root, text="Last Name").grid(row = 2)
eLName = tk.Entry(root)
eLName.grid(row = 2, column = 1)

#color
lblColor = tk.Label(root, text="Color").grid(row = 3)
eColor = tk.Entry(root)
eColor.grid(row = 3, column = 1)

#Quit button
btnQuit = tk.Button(root,
                   text="Quit",
                   fg="red",
                   command=quit)
btnQuit.grid(row = 3, column = 4)

#Enter Button
btnShow = tk.Button(root,
                    text = "Show",
                    command = lambda: returnStudent(eLName.get()))
btnShow.grid(row = 2, column = 4)



root.mainloop()
