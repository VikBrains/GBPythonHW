""" ----4- Проект «Склад оргтехники».
Создать класс, описывающий склад.
Создать класс «Оргтехника», который будет базовым для классов-наследников.
Создать классы-наследники — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
--------5- Продолжить работу над предыдущим заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу её в
    определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники и других,
    можно использовать любую подходящую структуру, например, словарь.
--------6- Продолжить работу над вторым предыдущим заданием.
Реализуйте механизм валидации вводимых пользователем данных. Например, Запрет
    использовать строковый тип данных для указания количества принтеров,
    отправленных на склад.
"""


class Warehouse:
    __storage = []
    __summary = {}

    def get(self, equipment):
        if not isinstance(equipment, OfficeEquipment):
            raise Exception('Склад может принимать только оргтехнику')
        self.__storage.append(equipment)
        if self.__summary.get(equipment.type) is not None:
            self.__summary[equipment.type] += 1
        else:
            self.__summary.setdefault(equipment.type, 1)

    def report_items(self):
        for item in self.__storage:
            print(item)

    def report_total(self):
        for k, v in self.__summary.items():
            print(f'{k}: {v} модели')


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
