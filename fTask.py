"""4. Представлен список чисел. Определите элементы списка, не имеющие
повторений. Сформируйте итоговый массив чисел, соответствующих требованию.
Элементы выведите в порядке их следования в исходном списке.
Для выполнения задания обязательно используйте List comprehension.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""



def a_counter(lst:list) -> dict:
    result = {}
    for key, el in enumerate(lst):
        if result.get(el) is None:
            result[el] = 1
        else:
            result[el] += 1
    return result

list_src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
count = a_counter(list_src)
list_res = [x for x, n in count.items() if n == 1]
print(list_res)
