# Created by Marcin "Cozoob" Kozub 03.08.2021

def get_prop(name_of_file, the_person):
    dictionary = {}
    persons_data = []

    with open(name_of_file, "r") as file:
        for line in file:
            tmp = line.split("->")
            tmp[1] = tmp[1].split(",")
            tmp[0] = tmp[0].strip()
            for i in range(len(tmp[1])):
                tmp[1][i] = tmp[1][i].strip()

            # print(tmp)
            if tmp[0] == the_person:
                persons_data = tmp[1].copy()

            for elem in tmp[1]:
                dictionary[elem] = dictionary.get(elem, 0) + 1

        # print(dictionary)
        the_data = []
        for key, val in dictionary.items():
            the_data.append([val, key])

        the_data.sort(reverse=True)
        # print(the_data)
        # print(persons_data)
        counter = 0
        i = 0
        # zamieniam persons_data na zbior zeby szybciej in dzialalo
        persons_data = set(persons_data)
        suggestions = []
        while counter < 5 or i < len(the_data):
            if not the_data[i][1] in persons_data:
                suggestions.append(the_data[i][1])
                counter += 1

            i += 1

        return suggestions

if __name__ == '__main__':
    print(get_prop("data.txt", "Martin Kozub"))
