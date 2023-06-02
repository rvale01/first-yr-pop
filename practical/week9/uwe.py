class Person:

    def __init__(self, firstName="X", lastName="X", address="Bristol"):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__address = address

    def setFirstName(self, firstName):
        self.__firstName = firstName

    def getFistName(self):
        return self.__firstName

    def setLasttName(self, lastName):
        self.__lastName = lastName

    def getLastName(self):
        return self.__lastName

    def setAddress(self, address):
        self.__address = address

    def getAddress(self):
        return self.__address

    def __str__(self):
        return "Name:" + self.getFistName() + ", Surname: " + self.getLastName() + ", Address: " + self.getAddress()


class Lecturer(Person):

    def __init__(self, firstName="X", lastName="X", address="Bristol", id=0):
        super().__init__(firstName, lastName, address)
        self.__id = id

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def __str__(self):
        return super().__str__() + " ID: " + str(self.getId())


class Student(Person):
    def __init__(self, firstName="X", lastName="X", address="Bristol", id=0):
        super().__init__(firstName, lastName, address)
        self.__id = id

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def __str__(self):
        return super().__str__() + ", Id: " + str(self.getId())


class GraduateStudent(Person):
    def __init__(self, firstName="X", lastName="X", address="Bristol", id=0, supervisor=""):
        super().__init__(firstName, lastName, address)
        self.__supervisor = supervisor
        self.__id = id

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getSupervisor(self):
        return self.__supervisor

    def setSupervisor(self, supervisor):
        self.__supervisor = supervisor

    def __str__(self):
        return super().__str__() + ", Supervisor: " + self.getSupervisor() + ", Id: " + str(self.getId())


class UnderGradaute(Student):
    def __init__(self, firstName="X", lastName="X", address="Bristol", id=0, subject=""):
        super().__init__(firstName, lastName, address, id)
        self.__subject = subject

    def getSubject(self):
        return self.__subject

    def setSubject(self, subject):
        self.__subject = subject

    def __str__(self):
        return super().__str__() + ", Subject: " + self.getSubject()


class PermanentLecturer(Lecturer):

    def __init__(self, firstName="X", lastName="X", address="Bristol", id=0, hours=0):
        super().__init__(firstName, lastName, address, id)
        self.__hours = hours

    def getHours(self):
        return self.__id

    def setHours(self, hours):
        self.__id = hours

    def __str__(self):
        return super().__str__() + " Hours: " + str(self.getHours())


class PartTimeLecturer(Lecturer):

    def __init__(self, firstName="X", lastName="X", address="Bristol", id=0, hours=0):
        super().__init__(firstName, lastName, address, id)
        self.__hours = hours

    def getHours(self):
        return self.__id

    def setHours(self, hours):
        self.__id = hours

    def __str__(self):
        return super().__str__() + " Hours: " + str(self.getHours())


class HRStaff(Person):

    def __init__(self, firstName="X", lastName="X", address="Bristol", id=0):
        super().__init__(firstName, lastName, address)
        self.__id = id

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def __str__(self):
        return super().__str__() + " ID: " + str(self.getId())

class Accountant(HRStaff):

    def __init__(self, firstName="X", lastName="X", address="Bristol", id=0, hours=0):
        super().__init__(firstName, lastName, address, id)
        self.__hours = hours

    def getHours(self):
        return self.__id

    def setHours(self, hours):
        self.__id = hours

    def __str__(self):
        return super().__str__() + " Hours: " + str(self.getHours())

# creating a Person object with default values

# 2.2
# print("Creating a Person object with default values")
# pers = Person()
# print("Printing")
# print(pers)

# print("Now setting the names and address")
# pers.setFirstName("Annalisa")
# pers.setLasttName("Lo giudice")
# pers.setAddress("UK")
# print()

# print("Printing...")
# print(pers)
# print()

# print("Creating another Person object by passing the values explicitly")
# pers2 = Person("Nicholas", "Lo Giudice", "UK")
# print("Printing...")
# print(pers2)
# print()

# 2.3
lecturer = Lecturer("Chris", "Simons", "UWE Frenchay Campus 4QXX", 2345)
print(lecturer)
print()

student = Student("Peter", "Miller", "UWE Frenchay Campus", 5678)
print(student)
print()

gradstudent = GraduateStudent(
    "Dan", "Fielding", "UWE Frenchay Campus", 6789, "Jim Smith")
print(gradstudent)
