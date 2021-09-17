# Created by Marcin "Cozoob" Kozub 17.07.2021

if __name__ == '__main__':

    how_many_rows = int(input("> "))
    row = "x"

    for i in range(0, how_many_rows):
        print(row, end="\n")
        row += "xx"