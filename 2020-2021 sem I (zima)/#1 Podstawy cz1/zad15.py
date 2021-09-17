# Created by Marcin "Cozoob" Kozub 18.07.2021
import os

if __name__ == '__main__':
    files = os.listdir()
    counter = 0
    for elem in files:
        last = len(elem)
        if elem[last - 3: last] == ".py":
            counter += 1
    print(counter)