class Warehouse:
    __storage = []
    __summary = {}

    def get(self, equipment):
        if not isinstance(equipment, OfficeEquipment):               # если equipment НЕ является OfficeEquipment
            raise Exception('Склад работает только с оргтехникой')           # поднимается исключение "...."
        self.__storage.append(equipment)        # (если является) добавить equipment на Хранение
        if self.__summary.get(equipment.type) is not None:        # Запрос get: Если Хранилище Не Пусто (уже содержит) данный тип equipment
            self.__summary[equipment.type] += 1                      # увеличить количество данного equipment на 1 единицу
        else:
            self.__summary.setdefault(equipment.type, 1)        # запрос на принятие в Хранилище нового типа equipment со значением 1 шт

    def report_items(self):          # репорт по девайсам на хранении
        for item in self.__storage:   # для девайса в Хранилище
            print(item)              # печать по штукам

    def report_total(self):                # репорт по подклассам (типам)
        for k, v in self.__summary.items():   # для кЛЮЧА и Значения
            print(f'{k}: {v} модели')            # печать по Словарю


class OfficeEquipment:
    def __init__(self, type: str, model: str, cost: float, qty: int):
        self.type = str(type)
        self.model = str(model)
        self.cost = float(cost)
        self.qty = int(qty)

    def __str__(self):
        return f"{self.type} | {self.model} | {self.cost} | {self.qty}"


class Printer(OfficeEquipment):
    def __init__(self, model: str, cost: float, qty: int, is_colorful: bool):
        self.is_colorful = is_colorful
        super().__init__('Принтер', model, cost, qty)


class Scanner(OfficeEquipment):
    def __init__(self, model: str, cost: float, qty: int, dpi: str):
        self.dpi = dpi
        super().__init__('Сканер', model, cost, qty)

    def __str__(self):
        return f"{self.type} | {self.model} | {self.cost} | {self.qty} |" \
               f" {self.dpi}"


class Copier(OfficeEquipment):
    def __init__(self, model: str, cost: float, qty: int, is_colorful:
    bool, dpi: str):
        self.is_colorful = is_colorful
        self.dpi = dpi
        super().__init__('МФУ', model, cost, qty)

    def __str__(self):
        return f"{self.type} | {self.model} | {self.cost} | {self.qty} | " \
               f"{self.dpi} | {self.is_colorful}"

products = []
for i in range(1, 9):
    print(f'Информация о товаре {i}')
    type = input('Тип устройства: ')
    model = input('Модель: ')
    price = float(input('Цена: '))
    qty = int(input('Количество: '))
    dpi = input('Разрешение: ')
    is_colorful = input('Цветность: ')

    products.append((i, {'тип устройства': type, 'модель': model, 'цена': price,
                         'количество': qty, 'разрешение': dpi,
                         'цветность': is_colorful}))
# print(products())

if __name__ == '__main__':
    mod_prin01 = Printer('Epson M1140', 7300.12, 5, True)
    mod_prin02 = Printer('Xerox C230V', 6600.99, 4, False)
    mod_scan01 = Scanner('Epson Perf V19', 15470.49, 9, '4800x4800')
    mod_scan02 = Scanner('Canon LiDE 300', 18049.45, 7, '2400x2400')
    mod_copi01 = Copier('Canon PIXMA  MG2540S', 6790.99, 48, True, '1200x1200')
    mod_copi02 = Copier('HP LaserJet Pro M428', 45950.49, 12, False, '4800x600')
    mod_copi03 = Copier('KYOCERA ECOSYS P2040', 27150.79, 50, False, '2400x600')

    wh = Warehouse()
    wh.get(mod_prin01)
    wh.get(mod_prin02)
    wh.get(mod_scan01)
    wh.get(mod_scan02)
    wh.get(mod_copi01)
    wh.get(mod_copi02)
    wh.get(mod_copi03)

    wh.report_items()
    wh.report_total()
