from student import students

def login_system():
    while True:
        print("\n===========Login System===========")
        
        user_id = input("Enter your Student ID to login: ")

        # Check if the provided ID matches any student ID
        for student in students:
            if student.idnum == user_id:
                print("\n===========Main Menu===========")
                print(f"Welcome, {student.name}!")
                return user_id
        
        print("Invalid Student ID. Please try again.")
