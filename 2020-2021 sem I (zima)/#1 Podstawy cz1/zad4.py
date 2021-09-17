# Created by Marcin "Cozoob" Kozub 17.07.2021

if __name__ == '__main__':

    # The all numbers from 0 to 100 that are divided by 3 and odd.
    for i in range(0, 101, 3):
        if i % 2 != 0:
            print(i, end=' ')
    print()