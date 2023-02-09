"""5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нём атрибут title (название) и Метод draw (отрисовка).
    Метод выводит сообщение «Запуск отрисовки».
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер):
-	в каждом классе реализовать переопределение метода draw;
-	для каждого класса метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для
каждого экземпляра."""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки ручкой {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки карандашом {self.title}")


class Marker(Stationery):
    def draw(self):
        print(f"Запуск отрисовки маркером {self.title}")


stationery = Stationery('кистью беличьей')
stationery.draw()

pen = Pen('гелевой')
pen.draw()

pencil = Pencil('для набросков')
pencil.draw()

handle = Marker('для стекла')
handle.draw()
