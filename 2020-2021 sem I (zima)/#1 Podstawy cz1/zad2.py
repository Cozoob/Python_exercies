# Created by Marcin "Cozoob" Kozub 17.07.2021
if __name__ == '__main__':
    try:
        a = int(input("> "))
        b = int(input("> "))
    except ValueError:
        print("Wrong arguments!")
        exit()

    print("sum is", a + b)