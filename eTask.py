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

print(f"Исходный файл:\n{text}\n")
print(f"Список:\n{report}\n")

with open('task_7.json', 'w', encoding='UTF-8') as json file:
    json.dumps(report, json_file, ensure_ascii=False)

json_report = json.dumps(report, ensure_ascii=False)
print(f"Json-объект:"\n{json_report}")
