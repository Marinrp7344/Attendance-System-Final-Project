import face_recognition as fr
import cv2 as cv
import os
import pickle

"""
Facial Extraction: 
    Has 3 diffrent parts:
    -Detection: It detects the face, gray scales it, and uses the haar cascade functionality
    to figure out the dimensions in which the face lies
    -Parameters: Draws a rectangle around the perimeters of the face to use later 
    -Extraction: Uses the set perimeters to crop and save the image into a different folder that will be used later for identification
"""
# -----VARIABLES----- #

peoplePresent = []
totalConfidence = []
mainDirectory = r"Project\Student_Encodings"
compareDirectory = r"Project\ExtractedFaces"

# ------METHODS------ #

"""
   Goes through each picture in the extracted picture's file
   and compares it against the student's images to determine whether a
   student is present in the photo
"""
def comapareFace():
    #acceses the file in the Photo's Taken directory and goes through each image
    for people in os.listdir(compareDirectory):
        #combines the images and sets a confidence and name arrays
        comparePath = os.path.join(compareDirectory, people)
        confidence = []
        name = []
        #reads the image and convert's the image colors and encodes it
        takenImage = cv.imread(comparePath)
        grayTakenImage = cv.cvtColor(takenImage, cv.COLOR_BGR2RGB)
        takenImage_encoded = fr.face_encodings(grayTakenImage)[0]
        #acceses the file in the Student's directory and goes through each file
        for student in os.listdir(mainDirectory): 
            #joins the path with a fie to access every individual student file
            newPath = os.path.join(mainDirectory, student)
            print(newPath)
            name.append(student)
            #counts the number of faces that match and don't to generate a confidence level
            rightFace = 0.0
            wrongFace = 0.0

            #accesses every image in individual student file
            for file in os.listdir(newPath):
                picklePath = os.path.join(newPath, file)
                with open(picklePath, 'rb') as f:
                    storedEncoding = pickle.load(f)
                result = fr.compare_faces([storedEncoding], takenImage_encoded)
                #counts the number on right or wrong faces depending on the results
                if(result[0] == True):
                    rightFace += 1
                elif(result[0] == False):
                    wrongFace += 1
            print(rightFace)
            print(wrongFace)
            #appends the confidence level to the array
            confidence.append(addConfidence(rightFace, wrongFace))
        #After going through each image in every file it determines if the person is present
        determinePresence(confidence, name)
    return peoplePresent
        
"""
   After going through each of the images in a file
   it adds the number of matches and divides it
   to get a percentage of how many photos matched
"""  
def addConfidence(rightFaces, wrongFaces):
    totalFaces = rightFaces + wrongFaces
    accuracy = rightFaces/totalFaces
    return accuracy

"""
   Goes through each of the confidence levels in the array 
   for each person and if the person's confidence level is high enough 
   they are determined to be present
"""  
def determinePresence(confidence, name):
    i = 0
    for conf in confidence:
        if(conf >= .60):
            peoplePresent.append(name[i])
            totalConfidence.append(conf)
            print("here")
        i += 1

#comapareFace()
#print(peoplePresent)
#print(totalConfidence)

cv.waitKey(0)
