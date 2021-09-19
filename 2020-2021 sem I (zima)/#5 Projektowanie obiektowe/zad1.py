# Created by Marcin "Cozoob" Kozub 19.09.2021
from uuid import uuid4


class Human:

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Student(Human):

    def __init__(self, first_name, last_name, address, student_ID, faculty = None, courses = None):
        super().__init__(first_name, last_name, address)
        self._student_ID = student_ID
        self.faculty = faculty
        self.courses = courses

    @property
    def student_ID(self):
        return self._student_ID

    @student_ID.setter
    def student_ID(self, new_ID):
        self._student_ID = new_ID