from student import students, StudentInfo

def display_menu():
    print("\n1. View your information")
    print("2. View other student's information")
    print("3. Register a new student (Admin only)")  # Optional, for admin purposes
    print("4. Print all students in the system")
    print("5. Exit")
    choice = input("Your choice: ")
    return choice

def view_student_info(student):
    """Display the logged-in student's information."""
    print("\nYour Information:")
    print(student)

def view_other_student_info(students):
    """Display options to view other students' information."""
    StudentInfo.display_choices(students)
    try:
        choice = int(input("Enter the number of the student you want to view: "))
        selected_student = StudentInfo.get_student_by_choice(students, choice)
        if selected_student:
            print("\nSelected Student Information:")
            print(selected_student)
    except ValueError:
        print("Please enter a valid number.")

def print_all_students(students):
    """Print all students in the system."""
    print("\nAll Students:")
    for student in students:
        print(student)

def options_menu(student):
    while True:
        choice = display_menu()

        if choice == '1':
            view_student_info(student)
        elif choice == '2':
            view_other_student_info(students)
        elif choice == '3':
            print("This option is not implemented.")
        elif choice == '4':
            print_all_students(students)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
