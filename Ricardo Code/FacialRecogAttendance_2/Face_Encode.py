import face_recognition as fr
import cv2 as cv
import os
import pickle


mainDirectory = r'C:\Users\Ricardo\OneDrive\Desktop\repos\FacialRecogAttendance\Students'
storedEncodings = r'C:\Users\Ricardo\OneDrive\Desktop\repos\FacialRecogAttendance\Encoded_Faces'
pickleStorage = 'C:/Users/Ricardo/OneDrive/Desktop/repos/FacialRecogAttendance/Encoded_Faces/'

for student in os.listdir(mainDirectory): 
            #joins the path with a fie to access every individual student file
            newPath = os.path.join(mainDirectory, student)
            num = 0
            #accesses every image in individual student file
            for img in os.listdir(newPath):
                
                # takes every individual image in each file and convert's the image colors and encodes it
                imagePath = os.path.join(newPath, img)
                image = cv.imread(imagePath)
                gray_Image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
                comparedImage_encoded = fr.face_encodings(gray_Image)[0]
                
                for fileName in os.listdir(storedEncodings):  
                    if(student == str(fileName)):
                        pickle.dump(comparedImage_encoded, open(pickleStorage + f"{student}/" + f"{num}.dat",'wb'))
                        num += 1
                        


                