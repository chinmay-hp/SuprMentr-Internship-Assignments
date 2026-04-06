# Student Data Manager

# Dictionary to store student data
students = {}

# Taking input for 5 students
for i in range(1, 6):
    print(f"\nEnter details for Student {i}:")
    name = input("Enter student name: ")
    marks = float(input("Enter student marks: "))
    
    students[name] = marks

# Printing student data
print("\n----- Student Records -----")
for name, marks in students.items():
    print(f"{name}: {marks}")

# Finding topper
topper = max(students, key=students.get)
print(f"\nTopper of the class: {topper} with {students[topper]} marks")

# Calculating class average
average = sum(students.values()) / len(students)
print(f"Class Average: {average:.2f}")

# Function to assign grades
def assign_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

# Printing grades
print("\n----- Student Grades -----")
for name, marks in students.items():
    grade = assign_grade(marks)
    print(f"{name}: {marks} marks → Grade {grade}")