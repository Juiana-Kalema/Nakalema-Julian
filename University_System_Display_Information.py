# Parent class: Person
class Person:
    def __init__(self, name, age, id_number):
        self.name = name
        self.age = age
        self.id_number = id_number

    def display_info(self):
        print(f'Name: {self.name}, Age: {self.age}, ID: {self.id_number}')


# Subclass: Student
class Student(Person):
    def __init__(self, name, age, id_number, course, year):
        super().__init__(name, age, id_number)
        self.course = course
        self.year = year

    def display_info(self):
        super().display_info()
        print(f'Course: {self.course}, Year: {self.year}')


# Subclass: Lecturer
class Lecturer(Person):
    def __init__(self, name, age, id_number, department, subjects):
        super().__init__(name, age, id_number)
        self.department = department
        self.subjects = subjects  # List of subjects

    def display_info(self):
        super().display_info()
        print(f'Department: {self.department}, Subjects: {", ".join(self.subjects)}')


# Subclass: Staff
class Staff(Person):
    def __init__(self, name, age, id_number, position, salary):
        super().__init__(name, age, id_number)
        self.position = position
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f'Position: {self.position}, Salary: {self.salary}')


# Create objects
student = Student('Nakalema Julian', 20, '2300713388', 'Software Engineering', 2)
lecturer = Lecturer('Dr.Nasser Kimbugwe ', 45, 'LEC54321', 'Networks', ['Web Development', 'Emerging Web Technologies'])
staff = Staff('Linda Brown', 35, 'STF67890', 'Registrar', 5000000)

# Display information
print('--- Student Information ---')
student.display_info()
print('\n--- Lecturer Information ---')
lecturer.display_info()
print('\n--- Staff Information ---')
staff.display_info()
