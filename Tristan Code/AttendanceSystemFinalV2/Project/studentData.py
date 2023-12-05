from Project.imageData import *

# Class stores information related to one singular students
class StudentData:

    # -----VARIABLES----- #

    name = ""
    txtFilePath = ""
    isPresentToday = False

    # -----CONSTRUCTORS----- #

    def __init__(self, name, txtFilePath):
        self.name = name
        self.txtFilePath = txtFilePath

    """ Return the name of the student """
    def GetName(self):
        return self.name
    
    """ Returns the path to the students attendance sheet """
    def GetAttendanceSheet(self):
        return self.txtFilePath

    """ Marks student as present """
    def Present(self):
        self.isPresentToday = True
    
    """ Marks student as absent """
    def Absent(self):
        self.isPresentToday = False

    """ Returns the students attendance for the day"""
    def IsPresent(self):
        return self.isPresentToday