# Created by Marcin "Cozoob" Kozub 18.07.2021

if __name__ == '__main__':

    num = input("> ")
    print("The number of digits: ", len(num))
    sum = 0
    num = int(num)
    while num > 0:
        sum += num % 10
        num //= 10
    print("The sum of digits: ", sum)