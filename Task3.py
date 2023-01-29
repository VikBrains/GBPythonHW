"""3.	Реализовать функцию my_func(), которая принимает три позиционных
аргумента и возвращает сумму наибольших двух аргументов."""


def my_func(a, b, c):
    if a > c and b > c:
        return a + b
    if a > b and c > b:
        return a + c
    if b > a and c > a:
        return b + c


try:
    v_r1 = int(input("a = "))
    v_r2 = int(input("b = "))
    v_r3 = int(input("c = "))
    print(f"Сумма двух наибольших:  {my_func(v_r1, v_r2, v_r3)}")
except ValueError:
    print("Ошибка")
else:
    print("The End")
