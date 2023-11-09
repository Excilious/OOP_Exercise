#Imports
from Programs.Person import Person

"""
    Students - A SubClass in which would inherit the attributes from the base
    class "Person". This subclass would use the super() method in which would transfer
    all attributes from the base class into the subclass.
"""

class Student(Person):

    #Constructor
    def __init__(self,Name:str,Age:int,Name_Of_School:str,Behavior:str,YearGroup:str,TutorGroup:str,Gender:str="O"):
        #Transfer of attributes from baseclass to subclass
        super().__init__(Name,Age,Gender)
        self.Behaviour = Behavior
        self.YearGroup = YearGroup
        self.TutorGroup = TutorGroup
        self.Name_Of_School = Name_Of_School

    #__repr__ - A reporting function that would print out the attributes from this class in this format.
    def __repr__(self):
        print(f'\nBehaviour: {self.Behaviour}\nYear Group: {self.YearGroup}\nTutor Group: {self.TutorGroup}\nSchool Name: {self.Name_Of_School}\n')
