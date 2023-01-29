"""6.	Реализовать функцию int_func(), принимающую слова из
строчных латинских букв и возвращающую их с прописной первой буквой. Н
апример, print(int_func(‘text’)) -> Text."""

def int_func(word):
    first_char = word[:1]
    tail = word[1:]
    title_char = first_char.upper()
    return title_char + tail


text = input("enter your word: ")
print(f"{int_func(text)}")
