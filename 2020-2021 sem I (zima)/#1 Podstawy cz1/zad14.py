# Created by Marcin "Cozoob" Kozub 18.07.2021

if __name__ == '__main__':

    num = int(input("> "))
    bin_num = ''
    while num > 0:
        if num % 2 == 0:
            bin_num += '0'
        else:
            bin_num += '1'
        num //= 2
    bin_num = bin_num[::-1]
    print(bin_num)