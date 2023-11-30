# GUI Imports
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# File Pathing Imports
import os, shutil

# Back-End Imports
from Project.classroomLogic import *
from Project.studentData import *
from Project.StudentFileSystem import *
from Project.Face_Extraction import *
from Project.Face_Recognition import *
from Project.Face_Encode import *

# ---------- FRONT END ----------

"""
Default GUI: Shows options for Adding, Deleting, And taking attendance
    - Add GUI: Show text box for entering student name and asking for a file path to image of student and button for DONE
    - Delete GUI: Show text box for entering student name and button for DONE
    - Attendance GUI: Shows all students in a row with two check marks by each student for Present and Absent
"""

# Class handles all logic related to the front-end of the application
class ClassroomGUI:

    # Construtor will display the DEFAULT GUI
    def __init__(self):

        #Create back-end logic class and file system
        self.classLogic = ClassroomLogic()
        self.studentFileSystem = Student_File()

        # Create variables
        self.folderPath = ""

        # Application initialization
        self.master = tk.Tk()
        self.master.title("Classroom Application")
        self.master.geometry("800x500")
        self.master.resizable(width = False, height = False)

        # Frame construction
        self.ConstructDefaultFrame()
        self.ConstructAddStudentFrame()
        self.ConstructRemoveStudentFrame()
        self.ConstructTakeAttendanceFrame()

        # Hide frames
        self.addStudentFrame.pack_forget()
        self.removeStudentFrame.pack_forget()
        self.takeAttendanceFrame.pack_forget()

        # Main loop
        self.master.mainloop()

# ---------- FRAME CONSTRUCTION METHODS ---------- #

    """
    Creates the default starting frame when booting up application
        - "Add Student" Button
            1. (FRONT-END) Hides default frame and loads Add Student Frame
        - "Remove Student" Button
            1. (FRONT-END) Hides default frame and loads Remove Student Frame
        - "Take Attendance" Button
            1. (FRONT-END) Hides default frame and loads Take Attendance Frame 
    """
    def ConstructDefaultFrame(self):

        self.defaultFrame = tk.Frame(self.master, 
                                     width = 700, 
                                     height = 65, 
                                     padx = 0,
                                     pady = 0,
                                     highlightbackground = "blue", 
                                     highlightthickness= 2)

        self.addStudent = tk.Button(self.defaultFrame, text = "Add Student", font = ("Arial", 12), command = self.LoadAddStudentFrame)
        self.addStudent.place(x = 30, y = 20, height = 25, width = 160)

        self.removeStudent = tk.Button(self.defaultFrame, text = "Remove Student", font = ("Arial", 12), command = self.LoadRemoveStudentFrame)
        self.removeStudent.place(x = 263, y = 20, height = 25, width = 160)

        self.takeAttendance = tk.Button(self.defaultFrame, text = "Take Attendance", font = ("Arial", 12), command = self.LoadTakeAttendanceFrame)
        self.takeAttendance.place(x = 496, y = 20, height = 25, width = 160)
        
        # Pack the frame
        self.defaultFrame.pack()

    """
    Creates the Add Student Frame which is displayed when a teacher wishes to add a student
        - Text Box: Student name entered here
        - "Select Image from file" Button ": Store path to students image
        - "Done" Button: 
            1. (BACK-END) Grabs data in both text boxes and stores it within a student class which is then sent to the studentList
            2. (FRONT-END Hides frame and loads the default frame
    """
    def ConstructAddStudentFrame(self):

        self.addStudentFrame = tk.Frame(self.master, 
                                        width = 700, 
                                        height = 400, 
                                        padx = 0,
                                        pady = 0,
                                        highlightbackground = "red", 
                                        highlightthickness = 2)

        # Get student first name
        self.addStudentFirstNameLabel = tk.Label(self.addStudentFrame, text = "Student first name:")
        self.addStudentFirstNameLabel.place(x = 10, y = 5)
        self.addStudentFirstNameEntry = tk.Entry(self.addStudentFrame)
        self.addStudentFirstNameEntry.place(x = 150, y = 5)

        # Get student last name
        self.addStudentLastNameLabel = tk.Label(self.addStudentFrame, text = "Student last name:")
        self.addStudentLastNameLabel.place(x = 10, y = 35)
        self.addStudentLastNameEntry = tk.Entry(self.addStudentFrame)
        self.addStudentLastNameEntry.place(x = 150, y = 35)

        # Get student picture from file explorer
        self.imageLabel = tk.Label(self.addStudentFrame, text = "Student image:")
        self.imageLabel.place(x = 10, y = 65)

        self.imagePathBtn = tk.Button(self.addStudentFrame, text = "Browse Files", command = self.BrowseFilesEventHandler)
        self.imagePathBtn.place(x = 150, y = 65)

        # Allow for data to be sent over and hide frame if everything is good
        self.addStudentBtn = tk.Button(self.addStudentFrame, text = "Add Student", command = self.AddStudentEventHandler)
        self.addStudentBtn.place(x = 610, y = 5)

        # Allow for user to exit frame at any time
        self.exitBtn = tk.Button(self.addStudentFrame, text = "Exit", command = self.ExitAddStudentEventHandler)
        self.exitBtn.place(x = 660, y = 360)

        #self.addStudentFrame.pack(pady = 20)

    """
    Creates all widgets needed for the remove student frame
        - Text Box: Enter students name
        - Done Button: 
            1. (BACK-END) Grabs data and checks if student is in class if so removes student from class
            2. (FRONT-END) Hides frame and loads the default frame
    """
    def ConstructRemoveStudentFrame(self):
        self.removeStudentFrame = tk.Frame(self.master, 
                                    width = 700, 
                                    height = 400, 
                                    padx = 0,
                                    pady = 0,
                                    highlightbackground = "yellow", 
                                    highlightthickness = 2)
        
        # Get student first name
        self.removeStudentFirstNameLabel = tk.Label(self.removeStudentFrame, text = "Student first name:")
        self.removeStudentFirstNameLabel.place(x = 10, y = 5)
        self.removeStudentFirstNameEntry = tk.Entry(self.removeStudentFrame)
        self.removeStudentFirstNameEntry.place(x = 150, y = 5)

        # Get student last name
        self.removeStudentLastNameLabel = tk.Label(self.removeStudentFrame, text = "Student last name:")
        self.removeStudentLastNameLabel.place(x = 10, y = 35)
        self.removeStudentLastNameEntry = tk.Entry(self.removeStudentFrame)
        self.removeStudentLastNameEntry.place(x = 150, y = 35)

        # Allow for data to be sent over and hide frame if everything is good
        self.removeStudentBtn = tk.Button(self.removeStudentFrame, text = "Remove Student", command = self.RemoveStudentEventHandler)
        self.removeStudentBtn.place(x = 590, y = 5)
        
        self.exitBtn = tk.Button(self.removeStudentFrame, text = "Exit", command = self.ExitRemoveStudentEventHandler)
        self.exitBtn.place(x = 660, y = 360)

        #self.removeStudentFrame.pack()

    """
    Creates all widgets needed for the Take Attendance frame
        - Box with all students names along with two check boxes for 
            1. Present
            2. Absent
        - Two image boxes showing the current students face being checked
            against the image of students in the current class environment 
    """
    def ConstructTakeAttendanceFrame(self):

        self.takeAttendanceFrame = tk.Frame(self.master, 
                                    width = 700, 
                                    height = 400, 
                                    padx = 0,
                                    pady = 0,
                                    highlightbackground = "yellow", 
                                    highlightthickness = 2)
    

        # Display labels for "Students", "Present", "Absent", and "Attendance Rate"
        self.namesLabel = tk.Label(self.takeAttendanceFrame, text = "Students", highlightbackground= "blue")
        self.namesLabel.place(x = 10, y = 5)
        
        self.presentLabel = tk.Label(self.takeAttendanceFrame, text = "Present", highlightbackground= "blue")
        self.presentLabel.place(x = 210, y = 5)
        
        self.absentLabel = tk.Label(self.takeAttendanceFrame, text = "Absent", highlightbackground= "blue")
        self.absentLabel.place(x = 300, y = 5)

        self.attendanceLabel = tk.Label(self.takeAttendanceFrame, text = "Attendance Rate", highlightbackground= "blue")
        self.attendanceLabel.place(x = 390, y = 5)

        # Take Attendance button
        self.takeAttendanceBtn = tk.Button(self.takeAttendanceFrame, text = "Take Attendance", command = self.TakeAttendanceEventHandler)
        self.takeAttendanceBtn.place(x = 590, y = 5)

        # Finish button when done taking attendance
        self.exitBtn = tk.Button(self.takeAttendanceFrame, text = "Exit", command = self.ExitTakeAttendanceEventHandler)
        self.exitBtn.place(x = 660, y = 360)

        #self.takeAttendanceFrame.pack()

    """
    Creates student widgets in the TakeAttendance frame 
        - Displays students name along with a check in the present or absent box
    """
    def ShowStudentsAttendance(self, students):
        self.nameLabel = []
        self.presentBox = []
        self.absentBox = []
        self.attendanceRateLabel = []
        yValue = 40

        for student in students:
            self.nLabel = tk.Label(self.takeAttendanceFrame, text = student.GetName())
            self.nLabel.place(x = 10, y = yValue)
            #self.nameLabel.append(self.nLabel)

            self.presentBox = tk.Checkbutton(self.takeAttendanceFrame)
            self.presentBox.place(x = 210, y = yValue)

            self.absentBox = tk.Checkbutton(self.takeAttendanceFrame)
            self.absentBox.place(x = 300, y = yValue)

            if(student.IsPresent()):
                self.presentBox.select()
            else:
                self.absentBox.select()

            self.attendanceRateLabel = tk.Label(self.takeAttendanceFrame, text = self.studentFileSystem.ReadAttendanceSheet(student))
            self.attendanceRateLabel.place(x = 390, y = yValue)

            yValue += 20


# ---------- HELPER METHODS ---------- #
        
    """Loads the Default frame of the gui""" 
    def LoadDefaultFrame(self):
        self.HideFrame()
        self.defaultFrame.pack()

    """Loads the AddStudent frame of the gui"""
    def LoadAddStudentFrame(self):
        self.HideFrame()
        self.addStudentFrame.pack()

    """Loads the RemoveStudent frame of the gui"""
    def LoadRemoveStudentFrame(self):
        self.HideFrame()
        self.removeStudentFrame.pack()

    """Loads the TakeAttendance frame of the gui"""
    def LoadTakeAttendanceFrame(self):
        self.HideFrame()
        self.takeAttendanceFrame.pack()

    """Hide a frame if that frame is within the winfo_manager (Current frame displayed)"""
    def HideFrame(self):
        if self.addStudentFrame.winfo_manager():
            self.addStudentFrame.pack_forget()
        elif self.removeStudentFrame.winfo_manager():
            self.removeStudentFrame.pack_forget()
        elif self.takeAttendanceFrame.winfo_manager():
            self.takeAttendanceFrame.pack_forget()
        else:
            self.defaultFrame.pack_forget()

    """Checks if string passed only had alphabetical characters"""
    def NameValid(self, name):
        if name.isalpha():
            return True
        return False
    
    """Checks if the image path returns a .jpg"""
    def FolderPathValid(self, path):
        splitPath = os.path.splitext(path)
        print(splitPath[1])
        if splitPath[1] == ".dir":
            return True
        return False
        
# ---------- EVENT METHODS ---------- #

    """Loads file explorer window when imagePathBtn button is pressed in AddStudent frame"""
    def BrowseFilesEventHandler(self):
        # Gets folder path 
        self.folderPath = filedialog.askdirectory(initialdir="/",
                                                title="Select a Folder")

    """Stores back-end data and loads proper front-end frame"""
    def AddStudentEventHandler(self):
        isNameValid = False
        isFolderPathValid = False
        fullName = ""

        # ---------- BACK-END ---------- #

        # Check if name is valid
        firstName = self.addStudentFirstNameEntry.get()
        lastName = self.addStudentLastNameEntry.get()
        if firstName != "" and lastName != "" and self.NameValid(firstName) and self.NameValid(lastName):
            isNameValid = True
        # Set full name
        fullName = firstName + "_" + lastName
        # Check if folder path is valid
        if os.path.exists(self.folderPath):
            isFolderPathValid = True

        # Create sub-paths for the student
        studentPath = self.studentFileSystem.getStudentPath(self.studentFileSystem.studentPath, fullName)
        studentEncodingsPath = self.studentFileSystem.getStudentPath(self.studentFileSystem.encodingsPath, fullName)

        # Path does not already exist. Load new student into database and return to default frame
        if isNameValid and isFolderPathValid and not self.studentFileSystem.PathExists(studentPath):
            # Add student directories
            self.studentFileSystem.addStudent(studentPath)
            self.studentFileSystem.addStudent(studentEncodingsPath)
            # Add images to students student folder and create a txt file
            self.studentFileSystem.addImages(self.folderPath, studentPath)
            self.studentFileSystem.addTxtFile(studentPath)
            # Send .img path for encodings needs (path to .img folder, path to student encodings folder)
            encodeFaces(studentPath, fullName)

            # ---------- FRONT-END ---------- #

            # Display that student was added
            messagebox.showinfo(None, fullName + " was added!")
            # Remove data from components and load default frame
            self.addStudentFirstNameEntry.delete(0, tk.END)
            self.addStudentLastNameEntry.delete(0, tk.END)
            self.LoadDefaultFrame()

         # ---------- FRONT-END ---------- #

        # Load pop-up message with proper failure warning
        else:
            # Warn that student already exists
            if self.studentFileSystem.PathExists(studentPath):
                messagebox.showwarning("Warning", "Student already within class!")
            # Warn that no name was entered 
            elif fullName == "_":
                messagebox.showwarning("Warning", "No name was entered!")
            # Warn that no folder was selected
            elif self.folderPath == "":
                messagebox.showwarning("Warning", "No folder was selected!")
            # Warn that name is not valid
            elif not isNameValid:
                messagebox.showwarning("Warning", "Name is not valid. Name must contain only alphabetical letters and no spaces.")
            # Warn the file path is not valid
            else:
                messagebox.showwarning("Warning", "File Path is not valid.")         

    """ Removes all data from the AddStudent frame and loads default frame"""
    def ExitAddStudentEventHandler(self):
        # Remove data from components and load default frame
        self.addStudentFirstNameEntry.delete(0, tk.END)
        self.addStudentLastNameEntry.delete(0, tk.END)
        self.LoadDefaultFrame()

    """Removes ALL data pertaining to a student"""
    def RemoveStudentEventHandler(self):
        isNameValid = False
        isExistingFile = False
        fullName = ""

        # ---------- BACK-END ---------- #

        # Checks if name is valid
        firstName = self.removeStudentFirstNameEntry.get()
        lastName = self.removeStudentLastNameEntry.get()
        if firstName != "" and lastName != "" and self.NameValid(firstName) and self.NameValid(lastName):
            isNameValid = True

        fullName = firstName + "_" + lastName

        # Get file paths
        sPath = r"Project\Students"
        ePath = r"Project\Student_Encodings"
        studentPath = self.studentFileSystem.getStudentPath(sPath, fullName)
        studentEncodingsPath = self.studentFileSystem.getStudentPath(ePath, fullName)

        # Check if name is valid and that all paths return a folder
        if isNameValid and self.studentFileSystem.PathExists(studentPath) and self.studentFileSystem.PathExists(studentEncodingsPath):
            # Remove student folders if file paths exist
            if(self.studentFileSystem.PathExists(studentPath) and self.studentFileSystem.PathExists(studentEncodingsPath)):
                self.studentFileSystem.removeStudent(studentPath)
                self.studentFileSystem.removeStudent(studentEncodingsPath)
                
            # ---------- FRONT-END ---------- #

            # Remove data from components and load default frame
            self.removeStudentFirstNameEntry.delete(0, tk.END)
            self.removeStudentLastNameEntry.delete(0, tk.END)
            self.LoadDefaultFrame()

        # ---------- FRONT-END ---------- #

        # ELSE display pop-up warning message
        else:
            # Warn that no name was entered 
            if fullName == "_":
                messagebox.showwarning("Warning", "No name was entered!")
            elif not isNameValid:
                messagebox.showwarning("Warning", "Name is not valid. Name must contain only alphabetical letters and no spaces.")
            else:
                messagebox.showwarning("Warning", "Files with that name do not exist!")

    """ Removes all data from the RemoveStudent frame and loads default frame"""
    def ExitRemoveStudentEventHandler(self):
        # Remove data from components and load default frame
        self.removeStudentFirstNameEntry.delete(0, tk.END)
        self.removeStudentLastNameEntry.delete(0, tk.END)
        self.LoadDefaultFrame()

    """
    Takes picture from current day loads it into indiviudal faces and takes student image data from the 
    back-end to do facial recognition checks to see which students are present and which students are absent
    """
    def TakeAttendanceEventHandler(self):
        # Get picture for current day
        # Upload picture to CurrentDayPicture directory

        Extractfaces()  # Extract faces from current day 
        facesNameArray = comapareFace() # Returns names of students who are in attendance from the extracted faces

        # Store a list of students names
        studentPaths = os.listdir(self.studentFileSystem.studentPath)

        # Create unique student classes
        students = []
        for studentPath in studentPaths:
            txtFilePath = self.studentFileSystem.studentPath + ("\\" + studentPath)
            studentData = StudentData(os.path.basename(studentPath), self.studentFileSystem.getStudentAttendanceSheetPath(txtFilePath))
            students.append(studentData)

        # Updates students attendance for the day
        for student in students:
            if facesNameArray.__contains__(student.GetName()):
                student.Present()
            else:
                student.Absent()

        # Update students attendance file
        for student in students:
            self.studentFileSystem.AppendToAttendanceSheet(student)

        # Display students on GUI
        self.ShowStudentsAttendance(students)

    """ Removes all data from the TakeAttendance frame and loads default frame"""
    def ExitTakeAttendanceEventHandler(self):
        # ---------- BACK-END ---------- #

        # Remove files from ExtractFaces directory
        self.studentFileSystem.removeImages(self.studentFileSystem.extractionPath)
        # Remove file from CurrentDayPicture directory

        # ---------- FRONT-END ---------- #
        
        # Remove all data pertaining to the front end of the TakeAttendance frame
        self.remove
        self.LoadDefaultFrame()