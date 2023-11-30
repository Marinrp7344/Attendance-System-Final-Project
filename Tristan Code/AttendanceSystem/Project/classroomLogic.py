from Project.studentData import *

# ---------- BACK END ----------

"""
Default GUI: 

    - Each button will refresh GUI to show a new GUI for the specific button pressed
    
    Add Student GUI:
    - Will store student data entered to a student object and send that to the classroom object. In the 
        position that a student with those exact parameters already exists a message will be popped saying 
        something like "STUDENT IS ALREADY IN YOUR CLASS PLEASE CHECK YOUR ENROLLMENT OF STUDENTS"
    - When DONE button is pressed the above statement will be executed 
    
    Delete Student GUI:
    - Will take data entered and check repository of students in the class and if a student with that name exists
        all data related to that student will be deleted. In the off chance that the student entered does not exist
        a messages will be popped up saying something like "STUDENT DOES NOT EXISTS PLEASE CHECK SPELLING OR CHECK
        ENROLLMENT OF STUDENTS"
    
    Take Attendance GUI:  
    - Will send attendance data to some type of attendance holder for students 
    - This attendance data can later be checked by professors
"""

# Stores the students and takes attendance (SHOULD ONLY EVER BE ONE INSTANCE)
# THERE WILL BE A FILE THAT STORES THE LIST OF STUDENTS IN THE CLASS WITH THERE ATTENDANCE
class ClassroomLogic:

    # -----VARIABLES----- #

    studentList = list()

    # ------METHODS------ #

    """Adds a students to the list"""
    def AddStudent(self, studentName, imagePath):
        student = StudentData(studentName, imagePath)
        # checks if student does not exist
        if self.studentList.count(student) == 0:
            print("Adding student one moment...")
            self.studentList.append(student)

    """Checks if a student with name passed already exists"""
    def StudentAlreadyExists(self, namePassed):
        for student in self.studentList:
            if(student.name == namePassed):
                return True
        return False
    
    """Prints student names to the console"""
    def ShowStudents(self):
        for student in self.studentList:
            print(student.name)

    # takes attendance 
    # FUNCTION MUST:
        # 1. Take an image of multiple students. 
        # 2. Seperate the faces in the image
        # 3. Encode each of the faces
        # 4. Check each face against the faces of the students
        # 5. For each face that is a match that student MUST be marked as present
    def TakeAttendance(self):
        dayOfWeek = input("Enter the day of the week: ")
        print("Taking attendance for " + dayOfWeek)

    # marks a student as present in there file
    def MarkPresent(self, name):
        print(name + "present")

    # marks a student as absent in there file
    def MarkAbsent(self, name):
        print(name + "absent")
