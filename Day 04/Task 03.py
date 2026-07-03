class Student:

    count = 0

    def __init__(self, name):
        self.name = name
        Student.count = Student.count + 1

student1 = Student("Ali")
student2 = Student("Ahmed")
student3 = Student("Sara")

print("Student 1:", student1.name)
print("Student 2:", student2.name)
print("Student 3:", student3.name)

print("Total Students:", Student.count)