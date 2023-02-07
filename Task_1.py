"""1. Создать программный файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка."""


file = open('task_01_rew.txt', 'w', encoding='UTF-8')
input_not_empty = True
while input_not_empty:
    line = input("введите текст или оставьте пустую строку: ")
    if line != '':
        file.write(line + '\n')
    else:
        input_not_empty = False

file.close()
