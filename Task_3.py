"""3. Создать текстовый файл (не программно). Построчно записать
фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии
этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

report = []
sum_salaries = 0
with open('task_3 state.txt', 'r', encoding='UTF-8') as file:
     strings = file.readlines()
     print("Оклады сотрудников")
     for word in strings:
         word_items = word.split(' ')
         report.append([word_items[0], int(word_items[1])])
         sum_salaries += int(word_items[1])
         print(f"{word_items[0]}: ${int(word_items[1])}")

print("\nСотрудники с окладом менее $20000")
[print(worker[0]) for worker in report if worker[1] < 20000]


print(f"Средний оклад сотрудников ${sum_salaries / len(report)}")
