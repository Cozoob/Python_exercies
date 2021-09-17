# Created by Marcin "Cozoob" Kozub 17.07.2021

if __name__ == '__main__':

    budget = int(input("> "))
    row = "x"

    while budget > 0:
        if budget - len(row) >= 0:
            print(row, end="\n")
            budget -= len(row)
            row += "xx"
        else:
            print("x", end='')
            budget -= 1