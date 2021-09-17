# Created by Marcin "Cozoob" Kozub 03.08.2021
import os


def find_file(name_of_file):
    files = os.listdir()

    for file in files:
        if name_of_file in file:
            name_of_file = name_of_file.strip().upper() + ".TXT\n"
            # print(name_of_file)
            with open(file, "r") as handle:

                to_print = []
                found = False
                for line in handle:
                    # print(line)
                    if line == name_of_file or found:
                        to_print.append(line)
                        found = True

                    if line == "---EOF---\n" and found:
                        break

            if not found:
                print("The file has not been found.")
            else:
                for elem in to_print:
                    print(elem, end="")



if __name__ == '__main__':
    find_file("tekst3")