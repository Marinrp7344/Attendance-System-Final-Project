# FACIAL RECOGNITION AND IMAGE PROCESSING IMPORTS
import cv2
import numpy as np
import face_recognition

# Stores image data for a singular student
class ImageData:

    imgLocation = ""
    studentImg = face_recognition
    faceLoc = face_recognition
    encodedImg = face_recognition

    def __init__(self, imgLocation):
        self.imgLocation = imgLocation
        self.studentImg = face_recognition.load_image_file(imgLocation)
        self.faceLoc = face_recognition.face_locations(self.studentImg)[0]
        self.encodedImg = face_recognition.face_encodings(self.studentImg)[0]