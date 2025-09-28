
student_marks = {
    "Samiksha": 85,
    "Abhineet": 92,
    "Raj": 78,
    "Priya": 88,
    "Amit": 95
}

name = input("Enter student's name: ")


if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print(f"Student '{name}' not found in the records.")
