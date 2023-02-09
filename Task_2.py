"""2. Реализовать класс Road (дорога).
-	определить атрибуты: length (длина), width (ширина);
-	значения атрибутов должны передаваться при создании экземпляра класса;
-	атрибуты сделать защищёнными;
Определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
•	использовать формулу: длина*ширина*масса асфальта для покрытия
    одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна
Проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т."""


class Road:

    def __init__(self, length, width, thickness, weight_1sm):
        self._length = length
        self._width = width
        self.thickness = thickness
        self.weight = weight_1sm

    def get_mass(self):
        mass = ((self._length * self._width * self.thickness * self.weight)
                //1000)
        return mass

r = Road(20, 5000, 5, 25)
print(r.get_mass(), "тонн")