from add_student import login_system
from student import StudentInfo, students
from add_student import login_system
from student import students
from options import options_menu

def main():
    user_id = login_system()  # User must log in before accessing the student options
    if user_id:  # Proceed only if login was successful
        # Find the logged-in student based on their ID
        logged_in_student = next((s for s in students if s.idnum == user_id), None)
        if logged_in_student:
            options_menu(logged_in_student)

if __name__ == "__main__":
    main()
