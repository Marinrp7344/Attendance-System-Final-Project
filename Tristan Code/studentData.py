from Project.imageData import *

# Class stores information related to one singular students
class StudentData:

    # -----VARIABLES----- #

    name = "name"
    studentImgData = ImageData

    # -----CONSTRUCTORS----- #

    def __init__(self, name, imagePath):
        self.name = name
        self.studentImgData = ImageData(imagePath)

    # -----METHODS----- #

    def GetImageData(self):
        return self.studentImgData