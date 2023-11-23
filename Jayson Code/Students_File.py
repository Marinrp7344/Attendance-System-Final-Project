import os
import shutil

class Student_File:

    #-----Methods-----#

    def getStudentPath(studentsFolderPath, firstName, lastName):
        
        # Creates Path to FirstName_LastName folder in the Students folder
        studentPath = (studentsFolderPath  + ("\\" + firstName + "_" + lastName))
        return studentPath

        
    def addStudent (firstName, lastName, studentPath):
        # Check if The Folder Already Exists
        if (os.path.exists(studentPath)):
            print("Student Already Exists")
        else:
            #Create The Students Folder
            os.mkdir(studentPath)

    def addImage(firstName, lastName, imagePath, studentPath):
        #Moves Image to Students Folder
        shutil.move(imagePath, studentPath)

    def removeStudent(studentPath):

        #Check if the Folder Exists
        if (os.path.exists(studentPath)):

            # Iterate over all files in the folder
            for filename in os.listdir(studentPath):
                file_path = os.path.join(studentPath, filename)
            
            # Check if the path is a file (not a subfolder)
            if os.path.isfile(file_path):
                # Delete the file
                os.remove(file_path)
            else:
                print("Error, There Might be a File in the Students File")

            #Remove the Folder
            os.rmdir(studentPath)
        else:
            print("Student Does not Exist")
