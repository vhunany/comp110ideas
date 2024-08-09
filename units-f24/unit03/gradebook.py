def add_student(students, name, grades):
    students[name] = grades
    print(f"Added student '{name}' with grades: {grades}")

def remove_student(students, name):
    if name in students:
        students.pop(name)
        print(f"Removed student '{name}'.")
    else:
        print(f"Student '{name}' not found.")

def list_students(students):
    print("Current list of students and their grades:")
    for name in students:
        print(f"- {name}: {students[name]}")

def average_grades(students):
    print("Average grades of each student:")
    for name in students:
        grades = students[name]
        total = 0
        for grade in grades:
            total += grade
        average = total / len(grades)
        print(f"- {name}: {average}")

def main():
    students = {}

    # Add students
    add_student(students, 'Alice', [85, 92, 78])
    add_student(students, 'Bob', [88, 79, 95])
    add_student(students, 'Charlie', [90, 85, 82])

    # List all students
    list_students(students)

    # Calculate average grades
    average_grades(students)

    # Remove a student
    remove_student(students, 'Bob')

    # List all students again to see the change
    list_students(students)

    # Calculate average grades again
    average_grades(students)

# Call the main function
main()
