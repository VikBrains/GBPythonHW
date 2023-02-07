"""2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке."""

with open('task_2 src.txt', 'r', encoding='UTF-8') as file:
    strings = file.readlines()
    print(f"Всего строк: {len(strings)}")
    for key, value in enumerate(strings):
        words = value.split(' ')
        print(f"Слов в строке {key + 1}: {len(words)}")
