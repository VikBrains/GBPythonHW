"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления
на ноль. Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой."""


class ZeroDivStop(Exception):
    def __init__(self, txt):
        self.txt = txt


def zero_div_checker():
    try:
        a = int(input('Введите делимое: '))
        b = int(input('Введите делитель: '))
        if b == 0:
            raise ZeroDivStop("задача не корректна, на '0' делить нельзя")
        else:
            res = a / b
            return res
    except ValueError:
        return "Вы не ввели цифры"
    except ZeroDivStop as err0r:
        return err0r

print(zero_div_checker())
