# Created by Marcin "Cozoob" Kozub 31.07.2021

if __name__ == '__main__':


    # zamiana recznie
    a = 1
    b = 2
    print(a, b)
    tmp = b
    b = a
    a = tmp
    print(a, b)

    # zamiana po pythonowsku
    a = 2
    b= 5
    print(a, b)
    a, b = b, a
    print(a, b)