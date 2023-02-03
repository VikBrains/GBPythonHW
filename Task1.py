"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта
заработной платы сотрудника. Используйте в нём формулу:
(выработка в часах*ставка в час) + премия. Во время выполнения
расчёта для конкретных значений необходимо запускать скрипт с параметрами."""

from sys import argv

script, work_hours, money_per_hour, bonus = argv

# example
work_hours = 168
money_per_hour = 8
bonus  = 55


def calc_salary(work_hours, money_per_hour, bonus):
    try:
        result = (float(work_hours) * float(money_per_hour) + float(bonus))
    except ValueError:
        return
    return result


print(f"{calc_salary(work_hours, money_per_hour, bonus)}")
