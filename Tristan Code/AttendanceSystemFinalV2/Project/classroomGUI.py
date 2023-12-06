# GUI Imports
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# File Pathing Imports
import os, shutil

# Back-End Imports
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
        self.studentFileSystem = Student_File()

        # Initialize variables
        self.students = []
        self.folderPath = ""
        self.imgPath = ""

        # Check if proper directories exist if not create them
        if not self.studentFileSystem.PathExists(self.studentFileSystem.studentPath):
            self.studentFileSystem.CreateDirectory(self.studentFileSystem.studentPath)
        if not self.studentFileSystem.PathExists(self.studentFileSystem.encodingsPath):
            self.studentFileSystem.CreateDirectory(self.studentFileSystem.encodingsPath)

        # Store a list of students names from directory path
        studentPaths = os.listdir(self.studentFileSystem.studentPath)
        # Create unique student classes from the students directory
        for studentPath in studentPaths:
            txtFilePath = self.studentFileSystem.studentPath + ("\\" + studentPath)
            studentData = StudentData(os.path.basename(studentPath), self.studentFileSystem.getStudentAttendanceSheetPath(txtFilePath))
            self.students.append(studentData)

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

        self.nameLabel = []
        self.presentBox = []
        self.absentBox = []
        self.attendanceRateLabel = []
        self.yValue = 40

        self.takeAttendanceFrame = tk.Frame(self.master, 
                                    width = 700, 
                                    height = 400, 
                                    padx = 0,
                                    pady = 0,
                                    highlightbackground = "yellow", 
                                    highlightthickness = 2)
    
        # ------ BOILER PLATE ------ #

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

        # Choose image of the day button
        self.takePictureBtn = tk.Button(self.takeAttendanceFrame, text = "Take Picture", command = self.BrowseImagesEventHandler)
        self.takePictureBtn.place(x = 614, y = 35)

        # Finish button when done taking attendance
        self.exitBtn = tk.Button(self.takeAttendanceFrame, text = "Exit", command = self.ExitTakeAttendanceEventHandler)
        self.exitBtn.place(x = 660, y = 360)

        # ------ STUDENT DATA ------ #

        for student in self.students:
            nLabel = tk.Label(self.takeAttendanceFrame, text = student.GetName(), name= "label_" + student.GetName())
            nLabel.place(x = 10, y = self.yValue)
            self.nameLabel.append(nLabel)

            pBox = tk.Checkbutton(self.takeAttendanceFrame, name= "pBox_" + student.GetName())
            pBox.place(x = 210, y = self.yValue)
            self.presentBox.append(pBox)

            aBox = tk.Checkbutton(self.takeAttendanceFrame, name= "aBox_" + student.GetName())
            aBox.place(x = 300, y = self.yValue)
            self.absentBox.append(aBox)

            self.yValue += 20

        #self.takeAttendanceFrame.pack()

    """ Adds a singular student to the take attendance frame"""
    def AddStudentToAttendance(self, student):
        nLabel = tk.Label(self.takeAttendanceFrame, text = student.GetName(), name= "label_" + student.GetName())
        nLabel.place(x = 10, y = self.yValue)
        self.nameLabel.append(nLabel)

        pBox = tk.Checkbutton(self.takeAttendanceFrame, name= "pBox_" + student.GetName())
        pBox.place(x = 210, y = self.yValue)
        self.presentBox.append(pBox)

        aBox = tk.Checkbutton(self.takeAttendanceFrame, name= "aBox_" + student.GetName())
        aBox.place(x = 300, y = self.yValue)
        self.absentBox.append(aBox)

        self.yValue += 20

    """ Removes a students from the attendance list """
    def RemoveStudentFromAttendance(self, student):

        # Remove from list
        for index, tmpStudent in enumerate(self.students):
            if tmpStudent.GetName() == student.GetName():
                self.nameLabel.remove(self.nameLabel[index])
                self.presentBox.remove(self.presentBox[index])
                self.absentBox.remove(self.absentBox[index])

        # Destroy widget
        for widgetName in self.takeAttendanceFrame.winfo_children():
            if str(widgetName) == ".!frame4.label_" + student.GetName():
                print(str(widgetName))
                widgetName.nametowidget(str(widgetName)).destroy()
            elif str(widgetName) == ".!frame4.pBox_" + student.GetName():
                print(str(widgetName))
                widgetName.nametowidget(str(widgetName)).destroy()
            elif str(widgetName) == ".!frame4.aBox_" + student.GetName():
                print(str(widgetName))
                widgetName.nametowidget(str(widgetName)).destroy()

        # Remove the student from the list
        self.students.remove(student)

    """ Updates the widgets of all students in the Take Attendance frame """
    def UpdateAttendanceSheet(self):
        yValue = 40
        for nLabel in self.nameLabel:
          nLabel.place(x = 10, y = yValue)
          yValue += 20
        yValue = 40
        for pBox in self.presentBox:
            pBox.place(x = 210, y = yValue)
            yValue += 20
        yValue = 40
        for aBox in self.absentBox:
            aBox.place(x = 300, y = yValue)
            yValue += 20

    """
    Creates student widgets in the TakeAttendance frame 
        - Displays students name along with a check in the present or absent box
    """
    def MarkAttendance(self):
        yValue = 40

        for index, student in enumerate(self.students):
            if student.IsPresent():
                self.presentBox[index].select()
            else:
                self.absentBox[index].select()

            aRateLabel = tk.Label(self.takeAttendanceFrame, text = self.studentFileSystem.ReadAttendanceSheet(student))
            aRateLabel.place(x = 415, y = yValue)
            self.attendanceRateLabel.append(aRateLabel)

            yValue += 20


# ---------- HELPER METHODS ---------- #
        
    """Loads the Default frame of the gui""" 
    def LoadDefaultFrame(self):
        self.HideFrame()
        self.defaultFrame.pack()

    """Loads the AddStudent frame of the gui and check if needed directories for frame exist"""
    def LoadAddStudentFrame(self):
        # Check if proper directories exist if not create them
        if not self.studentFileSystem.PathExists(self.studentFileSystem.studentPath):
            self.studentFileSystem.CreateDirectory(self.studentFileSystem.studentPath)
        if not self.studentFileSystem.PathExists(self.studentFileSystem.encodingsPath):
            self.studentFileSystem.CreateDirectory(self.studentFileSystem.encodingsPath)

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
            
# ---------- EVENT METHODS ---------- #

    """
    Loads file explorer window when imagePathBtn button is pressed in AddStudent frame.
    This event allows the user to choose a folder which then stored the folder path in folderPath.
    """
    def BrowseFilesEventHandler(self):
        # Gets folder path 
        self.folderPath = filedialog.askdirectory(initialdir="/",
                                                title="Select a Folder")

    """
    Loads file explorer window when takePictureBtn is pressed in TakeAttendance frame.
    This event allows the user to choose a .jpg file from a folder which then stores the folder path in imagePath.
    """
    def BrowseImagesEventHandler(self):
        self.imgPath = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Image files",
                                                        "*.jpg*"),
                                                       ("all files",
                                                        "*.*")))

    """Stores back-end data and loads proper front-end frame"""
    def AddStudentEventHandler(self):
        isNameValid = False
        isFolderPathValid = False
        fullName = ""

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

        # Generate sub-direcotries for students from directories Students && Student_Encodings
        studentPath = self.studentFileSystem.getStudentPath(self.studentFileSystem.studentPath, fullName)
        studentEncodingsPath = self.studentFileSystem.getStudentPath(self.studentFileSystem.encodingsPath, fullName)

        # Check if name/paths are valid and that paths do not already exist
        if isNameValid and isFolderPathValid and not self.studentFileSystem.PathExists(studentPath):
            # Create and add unique student to the students list
            txtFilePath = self.studentFileSystem.studentPath + ("\\" + fullName)
            print(studentPath)
            studentData = StudentData(os.path.basename(studentPath), self.studentFileSystem.getStudentAttendanceSheetPath(txtFilePath))
            self.students.append(studentData)

            # Generate student directories with paths generates
            self.studentFileSystem.addStudent(studentPath)
            self.studentFileSystem.addStudent(studentEncodingsPath)

            # Add images from folder selected and generate students attendance sheet. Store in Student Sub-Directory.
            self.studentFileSystem.addImages(self.folderPath, studentPath)
            self.studentFileSystem.addAttendanceSheet(studentPath)

            # Send Students directory path for encodings along with there name
            encodeFaces(studentPath, fullName)

            # Generate new info widgets for student on TakeAttendance frame
            self.AddStudentToAttendance(studentData)

            # Display that student was added
            messagebox.showinfo(None, fullName + " was added!")

            # Remove data from child widgets of AddStudent frame
            self.addStudentFirstNameEntry.delete(0, tk.END)
            self.addStudentLastNameEntry.delete(0, tk.END)

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
        # Remove data from child widgets of AddStudent frame and load Default frame
        self.addStudentFirstNameEntry.delete(0, tk.END)
        self.addStudentLastNameEntry.delete(0, tk.END)
        self.LoadDefaultFrame()

    """Removes ALL data pertaining to a student"""
    def RemoveStudentEventHandler(self):
        isNameValid = False
        isExistingFile = False
        fullName = ""

        # Checks if name is valid
        firstName = self.removeStudentFirstNameEntry.get()
        lastName = self.removeStudentLastNameEntry.get()
        if firstName != "" and lastName != "" and self.NameValid(firstName) and self.NameValid(lastName):
            isNameValid = True

        # Set full name
        fullName = firstName + "_" + lastName

        # Obtain proper directory paths for student directories (Student Directory && Student_Encodings Directory)
        studentPath = self.studentFileSystem.getStudentPath(self.studentFileSystem.studentPath, fullName)
        studentEncodingsPath = self.studentFileSystem.getStudentPath(self.studentFileSystem.encodingsPath, fullName)

        # Check if name is valid and that all students data directories are valid
        if isNameValid and self.studentFileSystem.PathExists(studentPath) and self.studentFileSystem.PathExists(studentEncodingsPath):
            # Remove student data directories
            self.studentFileSystem.removeStudent(studentPath)
            self.studentFileSystem.RemoveStudentEncodings(studentEncodingsPath)

            # Find student for removal
            for student in self.students:
                if student.GetName() == fullName :
                    tmpStudent = student

            # Remove student from TakeAttendance frame and update TakeAttendance frame
            self.RemoveStudentFromAttendance(tmpStudent)
            self.UpdateAttendanceSheet()

            # Remove data from child widgets of RemoveStudent frame
            self.removeStudentFirstNameEntry.delete(0, tk.END)
            self.removeStudentLastNameEntry.delete(0, tk.END)

        # ELSE display proper pop-up warning message
        else:
            # Warn that no name was entered 
            if fullName == "_":
                messagebox.showwarning("Warning", "No name was entered!")
            # Warn that name entered is not valid
            elif not isNameValid:
                messagebox.showwarning("Warning", "Name is not valid. Name must contain only alphabetical letters and no spaces.")
            # Warn that data directories for name do not exists
            else:
                messagebox.showwarning("Warning", "Files with that name do not exist!")

    """ Removes all data from the RemoveStudent frame and loads default frame"""
    def ExitRemoveStudentEventHandler(self):
        # Remove data from child widgets of RemoveStudent frame and load Default frame
        self.removeStudentFirstNameEntry.delete(0, tk.END)
        self.removeStudentLastNameEntry.delete(0, tk.END)
        self.LoadDefaultFrame()

    """
    Takes picture from current day loads it into indiviudal faces and takes student image data from the 
    back-end to do facial recognition checks to see which students are present and which students are absent
    """
    def TakeAttendanceEventHandler(self):
        # Check if picture was taken and that path is to a .jpg. Lastly check that there are students within the class
        if self.imgPath != "" and self.studentFileSystem.ImagePathValid(self.imgPath) and self.students.__len__() > 0:
            # Upload picture to CurrentDayPicture directory
            self.studentFileSystem.AddImgOfTheDay(self.imgPath)

            # Extract faces from current day image and store names of students in attendance
            Extractfaces(self.imgPath, self.studentFileSystem.extractionPath)
            facesNameArray = comapareFace()

            # Updates students attendance for the day
            for student in self.students:
                if facesNameArray.__contains__(student.GetName()):
                    student.Present()
                else:
                    student.Absent()

            # Update students attendance file
            for student in self.students:
                self.studentFileSystem.AppendToAttendanceSheet(student)

            # Display students on GUI
            self.MarkAttendance()
        
        # Warn that no students are within the class
        elif self.students.__len__() == 0:
            messagebox.showwarning("Warning", "No students within class please add students to class.")

        # Warn that no picture was taken for the day
        else:
            messagebox.showwarning("Warning", "Picture was not taken/Img not selected.")

    """ Removes all data from the TakeAttendance frame and load default frame"""
    def ExitTakeAttendanceEventHandler(self):

        if self.attendanceRateLabel.count != 0:
            # ---------- BACK-END ---------- #

            # Remove files from ExtractFaces directory
            self.studentFileSystem.removeImages(self.studentFileSystem.extractionPath)
            # Remove file from CurrentDayPicture directory
            self.studentFileSystem.removeImages(self.studentFileSystem.imgOfTheDayPath)

            # ---------- FRONT-END ---------- #
            
            # Remove all data pertaining to the front end of the TakeAttendance frame
            for pBox in self.presentBox:
                pBox.deselect()

            for aBox in self.absentBox:
                aBox.deselect()

            for attendanceRate in self.attendanceRateLabel:
                attendanceRate.destroy()

        self.LoadDefaultFrame()