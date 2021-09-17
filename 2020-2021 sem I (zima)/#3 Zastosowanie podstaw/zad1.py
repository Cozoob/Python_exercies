# Created by Marcin "Cozoob" Kozub 03.08.2021

import os

def opt():
    files = os.listdir()
    files.sort()
    # print(files)
    new_string = ""
    new_name = ""
    for elem in files:
        if not elem.endswith(".txt"):
            continue
        else:
            with open(elem, "r") as file:
                new_string = new_string + elem.upper() + "\n\n" + file.read() + "\n\n" + "---EOF---" + "\n\n"
                elem = elem[0:len(elem) - 4]
                # print(elem)
                if new_name == "":
                    new_name = elem
                else:
                    new_name = new_name + "_" + elem

            # Now we can delete these useless files.
            os.remove(elem + ".txt")


    # print(new_string)
    # print(new_name)
    with open(new_name + ".txt", "w") as new_file:
        new_file.write(new_string)

    print("DONE")




if __name__ == '__main__':
    opt()