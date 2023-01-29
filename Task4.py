"""4.	Программа принимает действительное положительное число x и
целое отрицательное число y. Выполните возведение числа x в степень y.
Задание реализуйте в виде функции my_func(x, y). При решении задания нужно
обойтись без встроенной функции возведения числа в степень
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение
в степень с помощью оператора **. Второй — более сложная реализация без
оператора **, предусматривающая использование цикла.
"""


def res_abs(x):
    return x if x >= 0 else x * -1


def my_pow(x, y):
    result = x
    for i in range(res_abs(y) - 1):
        result *= x
    if y < 0:
        result = 1 / result
    return result


try:
    basis = int(input("x = "))
    degree = int(input("y = "))
    print(f"x ** y =  {my_pow(basis, degree)}")
except ValueError as e:
    print(e)

# вариант прямого возведения в степень

my_func = lambda base, degree: base ** degree
base = int(input("x = "))
degree = int(input("y = "))
print(my_func(base, degree))