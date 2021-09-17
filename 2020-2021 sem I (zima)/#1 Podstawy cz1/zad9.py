# Created by Marcin "Cozoob" Kozub 17.07.2021
from random import randint

if __name__ == '__main__':
    my_list = [randint(-5,20) for _ in range(10)]
    print("Lista przed przefiltrowaniem: ", my_list)

    i = 0
    while i < len(my_list):
        elem = my_list[i]
        if elem < 10:
            # my_list.__delitem__(i) # dziala identycznie
            my_list.remove(elem)
        else:
            i += 1

    print("Lista po filtrowaniu: ", my_list)