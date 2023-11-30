import os
import shutil
import pathlib
import glob
from datetime import date

class Student_File:

    #-----Variables-----#
    studentPath = r"Project\Students"
    encodingsPath = r"Project\Student_Encodings"
    extractionPath = r"Project\ExtractedFaces"

    #-----Methods-----#

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
            print(destinationFolder + fileName)
            shutil.copy(file, destinationFolder + ("\\" + fileName))

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

            os.removedirs(destinationFolder)

    """ Adds a txt file to the students folder"""
    def addTxtFile(self, destinationFolder):
        open(destinationFolder + ("\\attendanceSheet.txt"), "x")

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

            pattern = "\*.dat"
            files = glob.glob(studentPath + pattern)

            # Iterate through each path and copy date to dst directory
            for file in files:
                fileName = os.path.basename(file)
                os.remove(studentPath + ("\\" + fileName))

            os.removedirs(studentPath)

    """ Checks if the file path passed exists. """
    def PathExists(self, path):
        if os.path.exists(path):
            return True
        return False
    
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
        with open(student.GetAttendanceSheet(), "r") as myfile:
            line = myfile.readline().split(",")
            line[1] = line[1].removesuffix("\n")
            print(line)
            if(line[1] == "1"):
                numPresent += 1
            numTotal += 1
        return numPresent.__str__() + "/" + numTotal.__str__()
            
            
        

