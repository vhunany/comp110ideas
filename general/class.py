# Function to add a student to a class
def add_student(classes, class_student_tuple):
    class_name, student_id = class_student_tuple
    if class_name not in classes:
        classes[class_name] = []
    classes[class_name].append(student_id)

# Function to remove a student from a class
def remove_student(classes, class_student_tuple):
    class_name, student_id = class_student_tuple
    if class_name in classes:
        if student_id in classes[class_name]:
            classes[class_name].remove(student_id)
            if not classes[class_name]:  # Remove class if no students left
                del classes[class_name]

# Function to display the attendance
def display_attendance(classes):
    for class_name, students in classes.items():
        print(f"{class_name}: {', '.join(students)}")

# Interactive loop
def main():
    classes = {}
    while True:
        print("\nOptions: ")
        print("1. Add student")
        print("2. Remove student")
        print("3. Display attendance")
        print("4. Quit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            class_name = input("Enter class name: ")
            student_id = input("Enter student ID: ")
            add_student(classes, (class_name, student_id))
        
        elif choice == '2':
            class_name = input("Enter class name: ")
            student_id = input("Enter student ID: ")
            remove_student(classes, (class_name, student_id))
        
        elif choice == '3':
            display_attendance(classes)
        
        elif choice == '4':
            print("Quitting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the main function to start the program
if __name__ == "__main__":
    main()
