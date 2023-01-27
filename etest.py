products = []
for i in range(1, 2):
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
