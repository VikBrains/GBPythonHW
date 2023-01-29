"""7.	Продолжение задания 6. В программу должна попадать строка из слов,
разделённых пробелом, состоящих из строчных латинских букв. Нужно сделать
вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Используйте написанную ранее (для з.6) функцию int_func()."""

def int_func(word):
    first_char = word[:1]
    tail = word[1:]
    title_char = first_char.upper()
    return title_char + tail


def int_func_ext(row):
    result = []
    words = row.split(' ')
    for item in words:
        result.append(int_func(item))
    return ' '.join(result)


s = input("Введите строку для редактирования:\n")
print(f"{int_func_ext(s)}")
