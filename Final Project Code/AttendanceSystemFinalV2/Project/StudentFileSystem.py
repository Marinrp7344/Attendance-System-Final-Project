import os
import shutil
import pathlib
import glob
from datetime import date

class Student_File:

    #-----Variables-----#
    studentPath = r"Project\Students"
    encodingsPath = r"Project\Student_Encodings"
    extractionPath = r"Project\Extracted_Faces"
    imgOfTheDayPath = r"Project\CurrentDayPicture"

    #-----Methods-----#

    """ Creates a directory at the given path"""
    def CreateDirectory(self, path):
        os.mkdir(path)

    """ Returns the correct pathing for a student folder"""
    def getStudentPath(self, studentsFolderPath, studentName):
        
        # Creates Path to FirstName_LastName folder in the Students folder
        studentPath = (studentsFolderPath  + ("\\" + studentName))
        return studentPath

    """ Returns the correct pathing to a student attendance sheet"""
    def getStudentAttendanceSheetPath(self, studentsPath):
        # Creates Path to FirstName_LastName folder in the Students folder
        studentPath = (studentsPath  + ("\\" + "attendanceSheet.txt"))
        return studentPath

    """ Adds a folder with the students name """    
    def addStudent (self, studentPath):
        # Check if The Folder Already Exists
        if (os.path.exists(studentPath)):
            print("Student Already Exists")
        else:
            #Create The Students Folder
            os.mkdir(studentPath)

    """ Adds .jpgs to students folder """
    def addImages(self, sourceFolder, destinationFolder):
        
        # Return list of file paths with givin pattern
        pattern = "\*.jpg"
        files = glob.glob(sourceFolder + pattern)

        # Iterate through each path and copy date to dst directory
        for file in files:
            fileName = os.path.basename(file)
            shutil.copy(file, destinationFolder + ("\\" + fileName))

    """ Removes a students folder """
    def removeStudent(self, studentPath):
        #Check if the Folder Exists
        if (os.path.exists(studentPath)):

            # Return list of file paths with givin pattern
            pattern = "\*.jpg"
            files = glob.glob(studentPath + pattern)

            # Iterate through each path and copy date to dst directory
            for file in files:
                fileName = os.path.basename(file)
                os.remove(studentPath + ("\\" + fileName))

            # Return list of file paths with givin pattern
            pattern = "\*.txt"
            files = glob.glob(studentPath + pattern)

            # Iterate through each path and copy date to dst directory
            for file in files:
                fileName = os.path.basename(file)
                os.remove(studentPath + ("\\" + fileName))

            os.removedirs(studentPath)

    """ Removes students facial encodings data folder """
    def RemoveStudentEncodings(self, studentPath):
            # Return list of file paths with givin pattern
            pattern = "\*.dat"
            files = glob.glob(studentPath + pattern)

            # Iterate through each path and copy date to dst directory
            for file in files:
                fileName = os.path.basename(file)
                os.remove(studentPath + ("\\" + fileName))

            os.removedirs(studentPath)

    """ Removes all images at the location passed"""
    def removeImages(self, destinationFolder):
        #Check if the Folder Exists
        if (os.path.exists(destinationFolder)):

            # Return list of file paths with givin pattern
            pattern = "\*.jpg"
            files = glob.glob(destinationFolder + pattern)

            # Iterate through each path and copy date to dst directory
            for file in files:
                fileName = os.path.basename(file)
                os.remove(destinationFolder + ("\\" + fileName))

    """ Adds a txt file to the students folder"""
    def addAttendanceSheet(self, destinationFolder):
        print(destinationFolder +"\\attendanceSheet.txt") 
        open(destinationFolder + ("\\attendanceSheet.txt"), "x")
    
    """ Writes to the students attendance sheet """
    def AppendToAttendanceSheet(self, student):
        with open(student.GetAttendanceSheet(), "a") as myfile:
            today = date.today().__str__() 
            if(student.IsPresent()):
                myfile.writelines(today + ",1\n")
            else:
                myfile.writelines(today + ",0\n")

    """ Returns a string of the students attendance rate """
    def ReadAttendanceSheet(self, student):
        numPresent = 0
        numTotal = 0
        file = open(student.GetAttendanceSheet(), "r")
        while file:
            line = file.readline()
            if line == "":
                break
            lineList = line.split(",")
            if lineList[1] == "1\n":
                numPresent += 1
            numTotal += 1
        file.close()
        return numPresent.__str__() + "/" + numTotal.__str__()
    
    """ Adds .jpg file to the destination folder """
    def AddImgOfTheDay(self, sourceFile):
        fileName = os.path.basename(sourceFile)
        shutil.copy(sourceFile, self.imgOfTheDayPath + ("\\" + fileName))

    """ Checks if the file path passed exists. """
    def PathExists(self, path):
        if os.path.exists(path):
            return True
        return False
            
    """ Checks if the path is a directory """
    def FolderPathValid(self, path):
        splitPath = os.path.splitext(path)
        if splitPath[1] == ".dir":
            return True
        return False
            
    """ Checks if the path is a .jpg"""
    def ImagePathValid(self, path):
        splitPath = os.path.splitext(path)
        if splitPath[1] == ".jpg":
            return True
        return False

