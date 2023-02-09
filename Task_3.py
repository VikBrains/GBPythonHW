"""3. Реализовать базовый класс Worker (работник).
-	определить атрибуты: name, surname, position (должность), income (доход);
-	атрибут income должен быть защищённым и ссылаться на словарь, содержащий
    элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
Создать класс Position (должность) на базе класса Worker; в нём реализовать
    методы получения полного имени сотрудника (get_full_name) и дохода с учётом
    премии (get_total_income);
Проверить работу примера на реальных данных: создать экземпляры класса Position
    передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: int,
                 bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


human = Position('Иван', 'Кузнецов', 'Менеджер', 100000, 20000)
print(human.get_full_name())
print(human.position)
print(human.get_total_income())
