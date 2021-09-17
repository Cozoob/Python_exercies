# Created by Marcin "Cozoob" Kozub 17.07.2021

if __name__ == '__main__':

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(i, "FizzBuzz")
        elif i % 3 == 0:
            print(i, "Fizz")
        elif i % 5 == 0:
            print(i, "Buzz")
        else:
            print(i)
