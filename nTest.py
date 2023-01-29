def full_sum(my_list):
    items_sum = 0
    for item in my_list:
        try:
            items_sum += float(item)
        except ValueError:
            continue
    return items_sum


def sum_end_string(s):
    s = s.replace('#', '')
    s = s.replace(',', '.')
    numbers = s.split(' ')
    return full_sum(numbers)


numbers_sum = 0

while True:
    numbers_string = input(
        "Введите числа, разделенных пробелом. "
        "Для завершения введите символ '#'\n"
    )
    numbers_sum += sum_end_string(numbers_string)
    if numbers_sum != 0:
        print(f"Сумма значений всех элементов {numbers_sum}")
    if numbers_string.count('#'):
        break
