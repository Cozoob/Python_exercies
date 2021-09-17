# Created by Marcin "Cozoob" Kozub 18.07.2021

if __name__ == '__main__':

    str = input("> ")
    sub_str = input("> ")

    counter = 0
    idx = []
    first = 0
    last = len(sub_str) - 1
    while last < len(str):
        if str[first: last + 1] == sub_str:
            counter += 1
            idx.append(first + 1)

        first += 1
        last += 1
    print(counter, "occurrences")
    print(idx)