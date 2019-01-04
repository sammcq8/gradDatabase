import initDatabase
import os
def RestartDatabase():
    if os.path.exists("GradDatabase.db"):
        os.remove("GradDatabase.db")
    initDatabase.startDatabase()
