"""2. Реализовать проект расчёта суммарного расхода ткани на производство
одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь
определённое название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост
(для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на
этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property."""

from abc import ABC


class Clothes(ABC):
    def __init__(self, name: str):
        self.name = name
        print(self.name)


class Coat(Clothes):
    def __init__(self, name: str, size: int):
        self.size = size
        super().__init__(name)
        print(f"размер {self.size}")

    @property
    def material(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, name: str, height: int):
        self.height = height
        super().__init__(name)
        print(f"рост {self.height}")

    @property
    def material(self):
        return round(2 * self.height + 0.3, 2)


if __name__ == '__main__':
    coat = Coat('Кашемировое пальто Классика', 56)
    print(coat.material)
    suit = Suit('Женский костюм с люрексом', 5)
    print(suit.material)
