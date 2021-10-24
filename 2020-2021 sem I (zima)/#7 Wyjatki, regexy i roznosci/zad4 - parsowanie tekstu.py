# Created by Marcin "Cozoob" Kozub 24.10.2021
import re

def find_pattern(text, dic, key):
    regex = key + r" " + r".[^a-z^A-Z]"
    with open(text, "r") as file:
        try:
            res = re.search(regex, file.read()).group()
            res = re.search(r"[+-][0-9].*|[0-9].*", res).group()
            dic[key] = dic.get(key, int(res))
        except AttributeError:
            dic[key] = dic.get(key, 0)

def parse_defense():
    result = dict()
    file = "defense.txt"
    find_pattern(file, result, r"AC")
    find_pattern(file, result, r"touch")
    find_pattern(file, result, r"flat-footed")
    find_pattern(file, result, r"hp")
    find_pattern(file, result, r"Will")
    find_pattern(file, result, r"Ref")
    find_pattern(file, result, r"Fort")

    return result



if __name__ == '__main__':
    print(parse_defense())