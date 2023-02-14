products = []
for i in range(1, 4):
    print(f"Информация о товаре {i}")
    product_name = input("Название: ")
    product_price = int(input("Цена: "))
    product_qty = int(input("Количество: "))
    product_measure = input("Единица измерения: ")
    products.append((i, {'название': product_name, 'цена': product_price,
                         'количество': product_qty, 'eд': product_measure}))



print(f"Исходные данные по товару: \n{products}")

product_names = []
product_prices = []
product_qty = []
product_measures = []
for i in products:
    product_names.append(i[1].get('название'))
    product_prices.append(i[1].get('цена'))
    product_qty.append(i[1].get('количество'))
    product_measures.append(i[1].get('eд'))

report = {
    'название': list(set(product_names)),
    'цена': list(set(product_prices)),
    'количество': list(set(product_qty)),
    'eд': list(set(product_measures))
}

print(f"Отчет по списку товаров: \n{report}")

# Исходные данные по товару:
# [(1, {'название': 'копир', 'цена': 25000, 'количество': 25, 'eд': 'шт'}), (2, {'название': 'сканер', 'цена': 10000, 'количество': 10, 'eд': 'шт'}), (3, {'название': 'принтер', 'цена': 15000, 'количество': 15, 'eд': 'шт'})]
# Отчет по списку товаров:
# {'название': ['копир', 'принтер', 'сканер'], 'цена': [25000, 10000, 15000], 'количество': [25, 10, 15], 'eд': ['шт']}

# Выстраивание данных от Пользователя в Словарь
