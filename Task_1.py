"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год». В рамках класса реализовать два
метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""

from datetime import date


class Data:
    def __init__(self, data):
        self.data = data.split('-')

    @staticmethod
    def valid(data):
        try:
            day, month, year = data.split('-')
            date(int(year), int(month), int(day))
            return 'Хорошая дата'
        except ValueError:
            return 'Такой даты в Календаре нет!'

    @classmethod
    def type(cls, data):
        try:
            day, month, year = [int(i) for i in data.split('-')]
            return f"{type(day), day}\n{type(month), month}\n{type(year), year}"
        except ValueError:
            return 'Неверный формат даты'


in_data = input("Введите дату в формате дд-мм-гггг: ")
print(Data.type(in_data))
print(Data.valid(in_data))
