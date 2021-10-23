# Created by Marcin "Cozoob" Kozub 17.07.2021

if __name__ == '__main__':

    try:
        how_many_rows = int(input("> "))
    except ValueError:
        print("The argument must be an integer!")
        exit()
    row = "x"

    for i in range(0, how_many_rows):
        print(row, end="\n")
        row += "xx"