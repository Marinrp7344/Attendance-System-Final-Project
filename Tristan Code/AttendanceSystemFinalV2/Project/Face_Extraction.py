import cv2 as cv
"""
Facial Extraction: 

    Has 3 diffrent parts:
    -Detection: It detects the face, gray scales it, and uses the haar cascade functionality
    to figure out the dimensions in which the face lies
    -Parameters: Draws a rectangle around the perimeters of the face to use later 
    -Extraction: Uses the set perimeters to crop and save the image into a different folder that will be used later for identification
"""
# -----VARIABLES----- #

#path = r"C:\Dev\VSCode_Workspace\Unix_Class\AttendanceSystem\Project\CurrentDayPicture\Cage100.jpg"
#storedPath = "C:/Dev/VSCode_Workspace/Unix_Class/AttendanceSystem/Project/ExtractedFaces/"
ePath = "Project/ExtractedFaces/"

# ------METHODS------ #

"""Detects the faces in a picture"""
def Extractfaces(picturePath, storedPath):
    i = 0
    image = cv.imread(picturePath)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    #'haarcascade_frontalface_default.xml'
    haar_cascade = cv.CascadeClassifier(r"Project\haarcascade_frontalface_default.xml")
    #haar_cascade = cv.CascadeClassifier(r"C:\Dev\VSCode_Workspace\Unix_Class\AttendanceSystem\Project\haarcascade_frontalface_default.xml")
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=15)
    DrawRectangle(faces_rect, image)
    for (x,y,w,h) in faces_rect:
        SaveFaces(image,ePath+str(i),x,y,w,h)
        i += 1    

""" Extracts and saves the faces in a set folder that will later 
    be acessed by  other functions in attendance checking
"""
def SaveFaces(image, name, x,y,w,h):
    imageCrop = image[y:y+h,x:x+w]
    imageCrop = cv.resize(imageCrop, (180,227))
    cv.imwrite(name+".jpg", imageCrop)

"""Draws a rectangle around the faces to indicate where the crops will take place"""
def DrawRectangle(rect, image):
    for (x,y,w,h) in rect:
        cv.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), thickness=2)