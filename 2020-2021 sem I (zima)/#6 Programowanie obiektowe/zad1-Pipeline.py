# Created by Marcin "Cozoob" Kozub 21.09.2021
from abc import ABC, abstractmethod


# "interface"
class Applicable(ABC):
    @abstractmethod
    def apply(self, num1):
        pass


class Multiply(Applicable):

    def __init__(self, num2):
        self.num2 = num2

    def apply(self, num1):
        return self.num2 * num1


class Add(Applicable):

    def __init__(self, num2):
        self.num2 = num2

    def apply(self, num1):
        return self.num2 + num1


class ConvertToString(Applicable):

    def apply(self, num1):
        return str(num1)


class Pipeline(Applicable):

    def __init__(self):
        self.operations_sequence = []

    def then(self, operation):
        self.operations_sequence.append(operation)
        return self

    def apply(self, num):
        output = num
        for operation in self.operations_sequence:
            output = operation.apply(output)
        return output


if __name__ == '__main__':
    print(Pipeline().then(Multiply(2)).then(Add(3)).then(ConvertToString()).apply(10))