# GUI Imports
import tkinter as tk
from tkinter import filedialog

# File Pathing Imports
import os

# Back-End Imports
from Project.classroomLogic import *

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

        #Create back-end logic variable
        self.classLogic = ClassroomLogic()

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
        self.doneBtn = tk.Button(self.addStudentFrame, text = "Done", command = self.AddStudentEventHandler)
        self.doneBtn.place(x = 10, y = 95)

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
        
        # Get student name
        self.removeStudentNameLabel = tk.Label(self.removeStudentFrame, text = "Enter student name:")
        self.removeStudentNameLabel.place(x = 10, y = 5)

        self.removeStudentEntry = tk.Entry(self.removeStudentFrame)
        self.removeStudentEntry.place(x = 150, y = 5)

        # Allow for data to be sent over and hide frame if everything is good
        self.doneBtn = tk.Button(self.removeStudentFrame, text = "Done", command = self.LoadDefaultFrame)
        self.doneBtn.place(x = 10, y = 30)
        
        # Pack the frame
        #self.removeStudentFrame.pack()

    """Creates all widgets needed for the Take Attendance frame
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
        
        # Display labels for "Students", "Present", and "Absent"
        self.nameLabel = tk.Label(self.takeAttendanceFrame, text = "Students", highlightbackground= "blue")
        self.nameLabel.place(x = 10, y = 5)
        
        self.presentLabel = tk.Label(self.takeAttendanceFrame, text = "Present", highlightbackground= "blue")
        self.presentLabel.place(x = 150, y = 5)
        
        self.absentLabel = tk.Label(self.takeAttendanceFrame, text = "Absent", highlightbackground= "blue")
        self.absentLabel.place(x = 200, y = 5)

        # Finish button when done taking attendance
        self.doneBtn = tk.Button(self.takeAttendanceFrame, text = "Done", command = self.LoadDefaultFrame)
        self.doneBtn.place(x = 650, y = 360)

        # Pack the frame
        #self.takeAttendanceFrame.pack()

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
    def ImagePathValid(self, path):
        splitPath = os.path.splitext(path)
        if splitPath[1] == ".jpg":
            return True
        return False
        
# ---------- EVENT METHODS ---------- #

    """Loads file explorer window when imagePathBtn button is pressed in AddStudent frame"""
    def BrowseFilesEventHandler(self):
        self.filepath = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Image files",
                                                        "*.jpg*"),
                                                       ("all files",
                                                        "*.*")))

    """Stores back-end data and loads proper front-end frame"""
    def AddStudentEventHandler(self):
        isNameValid = False
        isImagePathValid = False
        fullName = ""

        # ---------- FRONT-END ---------- #

        # Checks if name is valid
        firstName = self.addStudentFirstNameEntry.get()
        lastName = self.addStudentLastNameEntry.get()
        if firstName != "" and lastName != "" and self.NameValid(firstName) and self.NameValid(lastName):
            isNameValid = True
            fullName = firstName + " " + lastName

        # Checks if image path is valid
        if self.imagePathBtn != "" and self.ImagePathValid(self.filepath):
                isImagePathValid = True

        # ---------- BACK-END ---------- #

        # Load new student into database and return to default frame
        if isNameValid and isImagePathValid and not self.classLogic.StudentAlreadyExists(firstName + " " + lastName):
            self.classLogic.AddStudent(fullName, self.filepath)
            self.classLogic.ShowStudents()
            self.addStudentFirstNameEntry.delete(0, tk.END)
            self.addStudentLastNameEntry.delete(0, tk.END)
            self.LoadDefaultFrame()

        # Load pop-up message with proper failure warning
        else:
            if not isNameValid:
                print("Name is not valid")
            else:
                print("File Path is not valid or file in not a .jpg file")         

    """Removes ALL data pertaining to a student from the back-end"""
    def RemoveStudentEventHandler(self):
        print("DOES NOTHING FOR NOW")   

    """
    Takes picture from current day loads it into indiviudal faces and takes student image data from the 
    back-end to do facial recognition checks to see which students are present and which students are absent
    """
    def TakeAttendanceEventHandler(self):
        print("DOES NOTHING FOR NOW")