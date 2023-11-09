"""
UserInterfaceModule - A Module in which would display userinterfaces as UI. Tkinter would be needed
(Set as default in tkinter library)

Abstraction - Using tkinter module, the class would create a new user interface for which should interface
with Main.py

Date - 06/11/23
"""

#Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

#!REMINDER - .mainloop() must be run on any object attached towards the class (SELF ATTRIBUTE = NEWWINDOWCREATION)
class UICreation:
    def __init__(self):
        self.NewWindowCreation = Tk()
        self.NewWindowCreation.geometry("700x500")

        self.FunctionAttributes = {
            "Create New Student":self._CreateNewUsers,
            "Create New Teacher":self._CreateTreeViewHeaders,
            "Search For A Subject":self._CreateTreeViewHeaders,
            "Removing A Student":self._CreateTreeViewHeaders,
            "Exporting A Teacher":self._CreateTreeViewHeaders,
        }

        self._CreateFrames()

    def _CreateNewUsers(self):
        Student_Attributes = [
            "Name","Age",
            "Salary","Subjects Taught",
            "Gender",
        ]
        
        for Type in Student_Attributes:
            if (Type == "Subjects Taught"):
                ...
            else:
                simpledialog.askstring(Type,f'Please enter the {Type}.')

    def _CreateTreeViewHeaders(self):
        ...

    def _CreateFrames(self):
        #A Container that would be the holder for the buttons
        _ToolBar = ttk.Frame(self.NewWindowCreation,width=1000)
        _ToolBar.grid(column=0,row=0)
        
        #Enumeration of the function attributes. Along with the function itself.
        for Index,Instance in enumerate(self.FunctionAttributes):
            _ButtonInstance = ttk.Button(_ToolBar,text=Instance,width=len(Instance)+2,command=self.FunctionAttributes[Instance])
            _ButtonInstance.grid(column=Index,row=0)

        #Treeview - a method within the ttk library which creates a new 
        #treeview frame. You can add headings and/or frames within the treeview
        UIListLayout = ttk.Treeview(self.NewWindowCreation,height=37)
        UIListLayout.place(x=0,y=30)

        #Creating sub columns for each instance

        #Testing
        for x in range(1,100):
            UIListLayout.insert('',index=x,text="TAG_"+str(x))


if __name__ == '__main__':
    NewUI = UICreation()
    NewUI.NewWindowCreation.mainloop()
