# Created by Marcin "Cozoob" Kozub 21.09.2021
from enum import IntEnum
from statistics import mean


class Grade(IntEnum):
    F = 1
    F_plus = 2
    E = 3
    E_plus = 4
    D = 5
    D_plus = 6
    C = 7
    C_plus = 8
    B = 9
    B_plus = 10
    A = 11

    def __str__(self):
        if "_plus" in self.name:
            return self.name.replace("_plus", "+")
        else:
            return self.name

    # for pretty printing lists of grades
    def __repr__(self):
        return self.__str__()


class GradeLog:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        self.grades = []



    def __str__(self):
        return f"The grade book of {self.first_name} {self.last_name}."

    def __repr__(self):
        return self.__str__()

    def add_grade(self, grade):
        self.grades.append(grade)


    def get_grades_average(self):
        avg = round(mean(self.grades))
        avg = Grade(avg)
        return str(avg)

if __name__ == '__main__':
    grade_log = GradeLog("Micheal", "Show")
    grade_log.add_grade(Grade.A)
    grade_log.add_grade(Grade.B_plus)
    grade_log.add_grade(Grade.C)

    print(grade_log)
    print(grade_log.get_grades_average())