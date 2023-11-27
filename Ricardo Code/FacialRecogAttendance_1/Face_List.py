import cv2 as cv
import os
"""
Facial Lists: 
    Make and manage a list of students in the class based on their files in the student directory
"""

#Will hold student names
students = []

#Updates the student list in an array and appends it to the student list file
def UpdateStudentList():
    student_list = open(r"StudentList.txt", "w")
    #Code that will go through each of the files in the student folders and take names on the files
    for files in os.listdir(r'C:\Users\Ricardo\OneDrive\Desktop\repos\FacialRecogAttendance\Students'):
        rawName = str(files)
        name = rawName.replace("_", " ")
        student_list.write(name+"\n")
        students.append(name)
    student_list.close()


