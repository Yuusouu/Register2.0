class StudentInfo:
    def __init__(self, name, age, idnum, email, phone):
        self.name = name
        self.age = age
        self.idnum = idnum
        self.email = email
        self.phone = phone

    def __repr__(self):
        return (f"StudentInfo(name='{self.name}', age='{self.age}', idnum='{self.idnum}', "
                f"email='{self.email}', phone='{self.phone}')")

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"ID: {self.idnum}\n"
                f"Email: {self.email}\n"
                f"Phone: {self.phone}\n")

    @staticmethod
    def display_choices(students):
        """Displays a list of students with options to choose from."""
        print("\nAvailable Students:")
        for index, student in enumerate(students, start=1):
            print(f"{index}. {student.name} (ID: {student.idnum})")
        print("0. Exit The Program")
        print()

    @staticmethod
    def get_student_by_choice(students, choice):
        """Returns a student object based on the user's choice."""
        if 1 <= choice <= len(students):
            return students[choice - 1]
        else:
            print("Invalid choice.")
            return None


# List of students with unique IDs
students = [
    StudentInfo("Mariano", "22", "2003-0-06213", "andreimariano@gmail.com", "09692312551"),
    StudentInfo("Nebril", "52", "2013-0-02713", "nebril555@gmail.com", "09691578452"),
    StudentInfo("Salongga", "22", "2021-0-06513", "andreimarinao555@gmail.com", "09694236785"),
    StudentInfo("Ete", "22", "2023-0-82312", "andreimarinao555@gmail.com", "09694238034"),
    StudentInfo("Ang", "22", "2022-0-02222", "andreimarinao555@gmail.com", "09695689567"),
    StudentInfo("Valzado", "22", "2017-0-02233", "andreimarinao555@gmail.com", "09695434768"),
    StudentInfo("Cruz", "22", "2023-0-02343", "andreimarinao555@gmail.com", "09694634526"),
    StudentInfo("Camacho", "22", "2013-0-15233", "andreimarinao555@gmail.com", "09697777777"),
    StudentInfo("Goot", "22", "2023-0-51213", "andreimarinao555@gmail.com", "09694573734"),
    StudentInfo("Torres", "22", "2002-0-15213", "andreimarinao555@gmail.com", "09695437790")
]
