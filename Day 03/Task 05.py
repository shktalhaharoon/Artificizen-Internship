students = [
    {"name": "Talha", "marks": 102},
    {"name": "Huzaifa", "marks": 101},
    {"name": "Ahmed", "marks": 99}
]

def get_marks(student):
    m=student["marks"]
    print(m)
    return m

result = sorted(students, key=get_marks)

print(result)