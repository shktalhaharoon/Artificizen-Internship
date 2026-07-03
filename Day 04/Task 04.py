class Student:

    def __init__(self, age):
        self.__age = age
    @property
    def age(self):
        return self.__age

student = Student(20)
print(student.age)