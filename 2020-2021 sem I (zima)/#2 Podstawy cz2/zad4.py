# Created by Marcin "Cozoob" Kozub 31.07.2021

def find_color(num1, num2, num3):
    found = False

    with open("colors.txt", "r") as file:

        for line in file:
            name_of_color, values = line.split(sep=":")
            # print(name_of_color)
            values = values.split()
            # print(values)
            if num1 == values[0] and num2 == values[1] and num3 == values[2]:
                found = True
                break

    if found:
        return name_of_color

    return None

if __name__ == '__main__':
    s = input("Give the 3 numbers (RGB) for color: ")
    s = s.split()
    print(find_color(s[0], s[1], s[2]))