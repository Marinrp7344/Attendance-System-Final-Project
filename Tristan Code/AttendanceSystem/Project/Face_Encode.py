import face_recognition as fr
import cv2 as cv
import os
import pickle

storedEncodings = r"Project\Student_Encodings"
pickleStorage = r"Project\Student_Encodings"

""" Encodes the images of all the faces"""
def encodeFaces(studentPath, studentName):
    #accesses every image in individual student file
    num = 0
    for img in os.listdir(studentPath):
        split = os.path.splitext(img)
        if(split[1] == ".jpg"):
            # takes every individual image in each file and convert's the image colors and encodes it
            imagePath = os.path.join(studentPath, img)
            image = cv.imread(imagePath)
            gray_Image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
            comparedImage_encoded = fr.face_encodings(gray_Image)[0]

            if(os.path.exists(storedEncodings + ("\\" + studentName))):
                    pickle.dump(comparedImage_encoded, open(pickleStorage + ("\\" + studentName + "/") + f"{num}.dat",'wb'))
                    num += 1


                