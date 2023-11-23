from msilib.schema import Feature
import os
import cv2 as cv
from cv2 import haveImageReader
import numpy as np
import face_recognition as fr

#Will hold student names
students = []

#Code that will go through each of the files in the student folders and take names on the files
for files in os.listdir(r'C:\Users\Ricardo\OneDrive\Desktop\repos\FacialRecogAttendance\Students'):
    students.append(files)

#creates the list of features and labels that will be used to train the facial recognition
def trainFaces():
     for student in students:
          label = student.index(students)
          print(label)
