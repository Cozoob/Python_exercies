# Created by Marcin "Cozoob" Kozub 08.08.2021

import shelve
import uuid
from datetime import datetime


class Employee:

    def __init__(self, first_name, last_name, age, PESEL='NONE', email='NONE', perm_lvl=0, db_ID = None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self._PESEL = PESEL
        self.email = email
        self.worked_hours = 8 * get_the_days()  # 8h per day => 8h*5=40 per week => 40h*4 = 160 h per month
        self.perm_lvl = perm_lvl    # 0 - the lowest; 1 - the middest; 2 - the highest

        if not db_ID:
            self._db_ID = str(uuid.uuid4())
        else:
            self._db_ID = db_ID



    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    @property
    def PESEL(self):
        return self._PESEL

    @PESEL.setter
    def PESEL(self, new_PESEL):
        self._PESEL = new_PESEL

    def check_perm_of(self, other):
        return other.perm_lvl

    def hours_left(self):
        return 160 - self.worked_hours

    def send_email_to(self, other):
        print(f"The email has been sent to {other.email} by {self.email}.")

    def save_to_db(self, database_name):
        with shelve.open(database_name) as db:
            db[self._db_ID] = self



class ITSupport(Employee):

    def __init__(self, first_name, last_name, age, PESEL='NONE', email='NONE', perm_lvl=1, tickets = None, db_ID = None):
        self.tickets = tickets
        super().__init__(first_name, last_name, age, PESEL, email, perm_lvl)


    def get_the_tickets(self):
        if self.tickets is None:
            return []
        return self.tickets

    def add_the_ticket(self, ticket):
        if self.tickets is None:
            self.tickets = [ticket]
        else:
            self.tickets.append(ticket)

    def delete_the_ticket(self, ticket):
        if not self.tickets is None:
            self.tickets.remove(ticket)

class Manager(Employee):

    def __init__(self, first_name, last_name, age, PESEL='NONE', email='NONE', perm_lvl=2, db_ID = None):
        super().__init__(first_name, last_name, age, PESEL, email, perm_lvl)
        self.worked_hours = 6 * get_the_days()

    def send_email_to_everyone(self, others):
        print("The email has been sent to ", end='')
        counter = len(others) - 1
        for person in others:
            print(person.email, end='')
            if counter > 0:
                print(", ", end='')
                counter -= 1

        print(" by " + self.email)




def get_the_days():
    curr = str(datetime.now()).split()
    curr = curr[0].split("-")
    curr = int(curr[2])
    weeks = curr // 7
    left_days = curr % 7
    if left_days == 6:
        left_days = 5

    return weeks * 5 + left_days


if __name__ == '__main__':
    jan_kowalski = Employee("Jan", "Kowalski", 40, "123123123", "jankowalski@gmail.com")
    rafal_januszko = Employee("Rafał", "Januszko", 18, "033170345", "rafaljanuszko@gmail.com")
    # jan_kowalski.save_to_db("database")
    # rafal_januszko.save_to_db("database")
    #
    print(rafal_januszko)
    print(jan_kowalski)

    rafal_januszko.send_email_to(jan_kowalski)

    print(rafal_januszko.first_name)
    print(rafal_januszko.check_perm_of(jan_kowalski))
    print()

    marcin_kozub = ITSupport("Marcin", "Kozub", 20, "012341234", "marcinkozub@gmail.com")
    print(marcin_kozub.worked_hours)
    marcin_kozub.add_the_ticket("Laptop R Januszko")
    print(marcin_kozub.get_the_tickets())
    print(marcin_kozub.perm_lvl)

    maxim_shevko = Manager("Maxim", "Shevko", 34, "NONE", "maximtheboss@gmail.com")
    maxim_shevko.send_email_to_everyone([rafal_januszko, jan_kowalski, marcin_kozub])
    print(maxim_shevko.perm_lvl)