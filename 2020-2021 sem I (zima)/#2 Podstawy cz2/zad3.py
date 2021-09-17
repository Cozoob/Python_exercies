# Created by Marcin "Cozoob" Kozub 31.07.2021

# Pomysl taki ze najpierw splituje stringa zeby podzielilo mi slowa po spacjach.
# Nastepnie przechodzac przez liste tworze/inkrementuje slownik pod odp. indeksem
# czyli slowem. Wybieram taki key ze max(d.values) w tym slowniku.

def find_the_famous_word(s):
    arr = s.split()
    d = {}
    for elem in arr:
        d[elem] = d.get(elem, 0) + 1

    max_val = -float("inf")
    answer = None
    for key, val in d.items():
        if max_val < val:
            max_val = val
            answer = key

    return answer


if __name__ == '__main__':
    s = "STOP STOP OK OK OK STOP OK AA BE CO STOP STOP"
    print(find_the_famous_word(s))