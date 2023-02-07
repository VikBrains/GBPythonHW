"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open('task_4 src.txt', 'r', encoding='UTF-8') as file_en:
    text_ru = file_en.read()
for en, ru in dictionary.items():
    text_ru = text_ru.replace(en, ru)

with open('task_4 res.txt', 'w', encoding='UTF-8') as file_ru:
    file_ru.write(text_ru)