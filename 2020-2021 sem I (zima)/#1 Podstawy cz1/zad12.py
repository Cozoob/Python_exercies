# Created by Marcin "Cozoob" Kozub 18.07.2021
from random import randint

if __name__ == '__main__':
    my_list = [randint(0, 10) for _ in range(10)]
    print(my_list)
    my_list.reverse()
    # my_list = my_list[::-1]
    print(my_list)