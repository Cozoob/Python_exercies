# Created by Marcin "Cozoob" Kozub 23.10.2021
import re

def no_warning(file):
    new_lines = []
    regex = "WARNING"
    for line in file:
        if not re.search(regex, line):
            new_lines.append(line)

    return new_lines

def check_connection_to_db(file):
    dbs = []
    regex = "connect"
    for line in file:
        if re.search(regex, line):
            db = line.split(":")
            db = db[len(db) - 1].strip()
            dbs.append(db[0:len(db)-1])

    return dbs

if __name__ == '__main__':
    with open("log.txt") as file:
        print(no_warning(file))

    with open("log.txt") as file:
        print(check_connection_to_db(file))
