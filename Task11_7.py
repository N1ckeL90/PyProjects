import re


class ComplexNumbers:
    def __init__(self, complex_num):
        self.complex_num = complex_num

    def __add__(self, other):
        real_num1 = self.find_real_numbers(self.complex_num)
        real_num2 = self.find_real_numbers(other.complex_num)
        real_part = int(real_num1.groups()[0]) + int(real_num2.groups()[0])
        imaginary_part = int(real_num1.groups()[1]) + int(real_num2.groups()[1])
        if imaginary_part >= 0:
            imaginary_part = f'+{imaginary_part}'
        return f'{real_part}{imaginary_part}i'

    def __mul__(self, other):
        real_num1 = self.find_real_numbers(self.complex_num)
        real_num2 = self.find_real_numbers(other.complex_num)
        real_part = int(real_num1.groups()[0]) * int(real_num2.groups()[0]) - int(real_num1.groups()[1]) * int(
            real_num2.groups()[1])
        imaginary_part = int(real_num1.groups()[0]) * int(real_num2.groups()[1]) + int(real_num1.groups()[1]) * int(
            real_num2.groups()[0])
        if imaginary_part >= 0:
            imaginary_part = f'+{imaginary_part}'
        return f'{real_part}{imaginary_part}i'

    def __str__(self):
        return self.complex_num

    @staticmethod
    def find_real_numbers(complex_num):
        tmp = complex_num.replace(' ', '')
        pattern_ = re.compile(r'(?P<real_part>[-]?\d+)(?P<imaginary_part>[+-]\d+)i', re.IGNORECASE)
        result = re.match(pattern_, tmp)
        return result


z1 = '2 + 3i'
z2 = '-1 + 1i'
complex_num1 = ComplexNumbers(z1)
complex_num2 = ComplexNumbers(z2)
print(complex_num1+complex_num2)
print(complex_num1*complex_num2)
