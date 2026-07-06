import json

students = [
    {
        "name": "Talha",
        "age": 24,
        "roll_number": 264,
        "major": "Science"
    },

    {
        "name": "Tuaha",
        "age": 19,
        "roll_number": 222,
        "major": "Arts"
    },

    {
        "name": "Haroon",
        "age": 18,
        "roll_number": 432,
        "major": "Science"
    },

    {
        "name": "Mamoon",
        "age": 20,
        "roll_number": 345,
        "major": "Arts"
    },

    {
        "name": "Yousaf",
        "age": 19,
        "roll_number": 567,
        "major": "Science"
    },

    {
        "name": "Faisal",
        "age": 18,
        "roll_number": 987,
        "major": "Arts"
    },

    {
        "name": "Hussain",
        "age": 20,
        "roll_number": 789,
        "major": "Science"
    }
]

# Open JSON file in write mode
file = open(r"C:\Users\LENOVO\OneDrive\Desktop\Artificizen_Internship\Day 05\student.json", "w")

# Save the list into the JSON file
json.dump(students, file, indent=4)

# Close the file
file.close()


# Open the JSON file in read mode
file = open(r"C:\Users\LENOVO\OneDrive\Desktop\Artificizen_Internship\Day 05\student.json", "r")

# Load data from the JSON file
data = json.load(file)

# Close the file
file.close()


# Display the student records
for student in data:
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Roll Number:", student["roll_number"])
    print("Major:", student["major"])
    print()