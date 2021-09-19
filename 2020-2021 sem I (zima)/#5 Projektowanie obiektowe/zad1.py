# Created by Marcin "Cozoob" Kozub 19.09.2021


class Human:

    def __init__(self, first_name, last_name, address, faculty=None, courses=None):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.faculty = faculty
        self.courses = courses

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(Human):

    def __init__(self, first_name, last_name, address, student_ID, faculty=None, courses=None):
        super().__init__(first_name, last_name, address, faculty, courses)
        self._student_ID = student_ID

    @property
    def student_ID(self):
        return self._student_ID

    @student_ID.setter
    def student_ID(self, new_ID):
        self._student_ID = new_ID


class Employee(Human):

    def __init__(self, first_name, last_name, address, employee_ID, faculty=None, courses=None):
        super().__init__(first_name, last_name, address, faculty, courses)
        self._employee_ID = employee_ID

    @property
    def employer_ID(self):
        return self._employee_ID

    @employer_ID.setter
    def employer_ID(self, new_ID):
        self._employee_ID = new_ID


class Lecturer(Employee):

    def __init__(self, first_name, last_name, address, employee_ID, vote_points, faculty=None, courses=None):
        super().__init__(first_name, last_name, address, employee_ID, faculty, courses)
        self.vote_points = vote_points


class University:

    def __init__(self, name, description=None, employees=None):
        self.name = name
        self.description = description
        self.employees = employees

    def add_employee(self, employee):
        if not self.employees:
            self.employees.add(employee)
        else:
            self.employees = {employee}


class Course(University):

    def __init__(self, name, ECTS, description=None, employees=None, students=None, faculty=None):
        super(Course, self).__init__(name, description, employees)
        self.ECTS = ECTS
        self.faculty = faculty
        self.students = students

    # argument student should be an object
    def add_student(self, student):
        if not self.students:
            self.students.add(student)
        else:
            self.students = {student}

    def remove_student(self, student):
        if not self.students:
            self.students.remove(student)


class Faculty(University):

    def __init__(self, name, internal_number, description=None, courses=None, employees=None):
        super(Faculty, self).__init__(name, description, employees)
        self._internal_number = internal_number
        self.courses = courses

    @property
    def internal_number(self):
        return self._internal_number

    @internal_number.setter
    def internal_number(self, new_internal_number):
        self._internal_number = new_internal_number


# Virtual Dean's Office
class DeanOffice(University):

    def __init__(self, name, description=None, employees=None, students=None, courses=None, faculties=None):
        super(DeanOffice, self).__init__(name, description, employees)
        self.students = students
        self.courses = courses
        self.faculties = faculties

    # argument student should be an object
    def add_new_student(self, student):
        if not self.students:
            self.students.add(student)
        else:
            self.students = {student}

    # argument student and course should be an object
    def add_student_to_course(self, student, course):
        if not student in course.students:
            course.add_student(student)
        else:
            print(f"{student.first_name} {student.last_name} is already in the course {course.name}.")

    # argument student should be an object
    def delete_student(self, student):
        for course in self.courses:
            if student in course:
                course.remove_student(student)

        self.students.remove(student)