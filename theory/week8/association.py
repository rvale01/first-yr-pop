class Lecturer:
    def __init__(self, name):
        self.name = name

    def getLecturerName(self):
        return self.name

    def setStudent(self, student):
        self.student = student

    def display(self):
        print("%s teaches %s" % (self.name, self.student.getStudentName()))

class Student:
    def __init__(self, name):
        self.name = name

    def getStudentName(self):
        return self.name

    def setLecturer(self, lecturer):
        self.lecturer = lecturer
    
    def display(self):
        print("%s is taught by %s" % \
        (self.name, \
        self.lecturer.getLecturerName()))

student1 = Student("Nick")
lecturer1 = Lecturer("Tim")

student1.setLecturer(lecturer1)
lecturer1.setStudent(student1)

student1.display()
lecturer1.display()


