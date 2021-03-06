# Created by Marcin "Cozoob" Kozub 17.07.2021

def what_operation(operation, num1, num2):
    if operation == "+":
        print("The sum of numbers is:", num1 + num2)
    elif operation == "-":
        print("The subtract of numbers is:", num1 - num2)
    elif operation == "*":
        print("The multiply of numbers is:", num1 * num2)
    elif operation == "^":
        print("The power of numbers is:", num1 ** num2)
    elif operation == "/":
        print("The division of numbers is:", num1 / num2)
    else:
        return True
    return False

if __name__ == '__main__':
    flag = True
    while flag:
        try:
            num1 = int(input("> "))
        except ValueError:
            print("The argument must be an integer.")
            continue
        operation = input("> ")
        try:
            num2 = int(input("> "))
        except ValueError:
            print("The argument must be an integer.")
            continue
        flag = what_operation(operation, num1, num2)
        if flag:
            print("The unknown operation.")