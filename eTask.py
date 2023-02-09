"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие
    атрибуты: speed, color, name, is_police (булево).
    и методы: go, stop, turn(direction), которые должны сообщать, что
        машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать
    текущую скорость автомобиля.
Переопределите метод show_speed для классов TownCar и WorkCar.
    При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
    сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""

#from termcolor import colored

#print(colored('Как поменять цвет?', 'red'))
#print('Как поменять цвет '+ colored('одного', 'green') +' слова?')


class Car:
    def __init__(self, color: str, name: str, is_police: bool):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f"мы поехали со скоростью {speed} км/ч")

    def stop(self):
        self.speed = 0
        print("мы остановились")

    def turn(self, direction: str):
        if self.speed > 0:
            print(f'поворачиваем {direction}')
        else:
            print("мы не можем поворачивать, мы стоим на месте")

    def show_speed(self):
        print(f"скорость машины {self.speed} км/ч")


class TownCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            up_speed = self.speed - 60
            print(f"Вы превысили скорость на {up_speed} км/ч")
        else:
            print(f"скорость машины {self.speed}")


class WorkCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            up_speed = (self.speed - 40)
            print(f'Вы превысили скорость на {up_speed} км/ч')
        else:
            print(f"скорость машины {self.speed}")


class SportCar(Car):
    def __init__(self, color: str, name: str):
#        super().__init__(color, name, is_police)
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False


class PoliceCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = True


def test_drive(automobile):
    print(
        f"- Тест-драйв автомобиля {automobile.name}, цвет {automobile.color}, "
        f"{'полицейский' if automobile.is_police else 'гражданский'}")
    automobile.go(50)
    automobile.show_speed()
    automobile.turn('направо')
    automobile.show_speed()
    automobile.stop()
    automobile.show_speed()
    automobile.turn('налево')
    automobile.go(70)
    automobile.show_speed()
    automobile.go(120)
    automobile.show_speed()
    automobile.stop()
    print("- Тест-драйв окончен", end="\n\n")


#car = Car('белый', 'Волга', False)
#print(car.go(70))
#print(car.turn("налево"))
#print(car.show_speed())
#test_drive(car)

smart = TownCar('мокрый асфальт', 'Smart')
test_drive(smart)

ferrari = SportCar('красный', 'Ferrari')
test_drive(ferrari)

gazel = WorkCar('зелёный', 'Газель')
test_drive(gazel)

mondeo = PoliceCar('бело-синий', 'Ford Mondeo')
test_drive(mondeo)
