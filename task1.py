"""1.	Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль."""
def divmod(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Деление на 0"
    return result


try:
    v_r1 = float(input("a = "))
    v_r2 = float(input("b = "))
    print(f"a / b = {divmod(v_r1, v_r2)}")
except ValueError:
    print("Неверный ввод")
