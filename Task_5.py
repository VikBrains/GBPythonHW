"""5. Создать (программно) текстовый файл, записать в него программно
набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран."""

import random

with open("task_5.txt", 'w', encoding='UTF-8') as file:
    space = ''
    for _ in range(7):
        file.write(space + str(random.randint(0, 10)))
        space = ' '

with open('task_5.txt', 'r', encoding='UTF-8') as file:
    numbers_str = file.read()
    numbers_list = numbers_str.split(' ')

print(f"Содержимое файла:\n{numbers_str}")
print(f"Сумма чисел:\n{sum([int(i) for i in numbers_list])}")
