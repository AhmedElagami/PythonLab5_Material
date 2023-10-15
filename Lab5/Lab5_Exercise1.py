
# ! classroom
# ? the classroom has:
    # * students => collection of students' names => strings
    # * classroom_number => a number to identify the class => class number 1

# ? you can add students 
# ? you can get students 
# ? you can display class information

# * we want to keep count of the classes

# ! Additional
# * we want to keep count of the classes in a better way
# * we want to use for loops to iterate through the class

#! concepts
#* iteration => how to make your class work in a for loop
#* default arguments

class Classroom:
    cnt = 0

    def __init__(self, classroom_number, students = []):
        self.__classroom_number = classroom_number
        self.__students = students
        Classroom.cnt += 1
    
    def addStudent(self, student):
        if(isinstance(student, str) and (len(student) != 0)):
            self.__students.append(student)
        else:
            print("Please enter a valid string as the student name!!")

    def getStudents(self): 
        return self.__students

    def displayClassroom(self):
        print(self)

    def __str__(self): 
        output = f"Class#{self.__classroom_number}\n"
        output += f"Students: {self.__students}"
        return output
    
    def __repr__(self):
        return self.__str__

    def __iter__(self):
        self.__currentIndex = 0
        return self

    def __next__(self):
        if(self.__currentIndex < len(self.__students)):
            result = self.__students[self.__currentIndex]
            self.__currentIndex += 1
            return result
        else: 
            raise StopIteration

    def printClassroomCnt():
        print(Classroom.cnt)

    # def iterateStudents(self):
    #     for student in self.__students:
    #         yield "newStudent"
    
def main():
    myFirstClass = Classroom(1, ["Ahmed", "Mark", "Tibor", "David"])

    mySecondClass = Classroom(1, ["Ahmed", "Mark", "Tibor", "David"])

    myThirdClass = Classroom(1, ["Ahmed", "Mark", "Tibor", "David"])

    #! Attribute 
    #* Thing  .   Attribute => can be a method or a variable 

    print(myFirstClass.cnt) #! instances can access class variables but a class can't access instance variables
    Classroom.printClassroomCnt()

    #! generators 

    # for student in myFirstClass.iterateStudents():
    #     print(student)

    for student in myFirstClass:
        print(student)

if __name__ == "__main__":
    main()













    