"""7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные
числа), выполните сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата."""


class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return ComplexNum(a, b)


    def __mul__(self, other):
        a = (self.a * other.a)
        b = (self.a * other.b)
        return ComplexNum(a, b)

    def __str__(self):
        return f'{self.a} + {self.b}j'


if __name__ == '__main__':
    z1 = ComplexNum(2, 5)
    z2 = ComplexNum(3, 6)
    z3 = z1 + z2
    z4 = z1 * z2

    print(f'z1 = {z1}')         # z1 = 2 + 5j
    print(f'z2 = {z2}')         # z2 = 3 + 6j
    print(f'z1 + z2 = {z3}')    # z1 + z2 = 5 + 11j
    print(f'z1 * z2 = {z4}')    # z1 * z2 = -24 + 27j
