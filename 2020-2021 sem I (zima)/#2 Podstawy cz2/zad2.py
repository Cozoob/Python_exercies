# Created by Marcin "Cozoob" Kozub 31.07.2021
from random import randint

def rand_dict(n):
    if n < 0 or n > 21:
        n = 21

    d = {randint(0, 20) : randint(0, 20) for _ in range(n)}
    return d

def reverse_dict(dictionary):
    new_d = {}
    for key, val in dictionary.items():
        new_d[val] = new_d.get(val, key)

    return new_d

if __name__ == '__main__':
    d = rand_dict(4)
    print(d)
    # print(rand_dict(-1))
    print(reverse_dict(d))