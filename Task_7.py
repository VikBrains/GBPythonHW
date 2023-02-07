"""7. Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка будет содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо
- построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю
прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать
_словарь с фирмами и их прибылями, а также
_словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
{“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

import json

report = []

with open('task_7 src.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    file.seek(0)
    profits = {}
    profit_sum = 0
    for line in text:
        el = line.split(' ')
        profit = int(el[2]) - int(el[3])
        if profit > 0:
            profits.update({el[0]: profit})
            profit_sum += profit
    report.append(profits)
    report.append({'average_profit': (profit_sum / len(profits))})

with open('task_7.json', 'w', encoding='UTF-8') as json file:
    json.dumps(report, json_file, ensure_ascii=False)

json_report = json.dumps(report, ensure_ascii=False)

print(f"Исходный файл:\n{text}\n")
print(f"Список:\n{report}\n")
print(f"Json-объект:"\n{json_report}")
