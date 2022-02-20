# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, 
# turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) 
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина едет.")

    def stop(self):
        print("Машина остановилась.")

    def turn(self, direction):
        print(f"Машина повернула на {direction}")

    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)   

    def show_speed(self):
        try:
            if int(self.speed) > 60:
                print(f"Скорость равна {self.speed}, она превышена!")
            else:
                print(f"Скорость равна {self.speed}")
        except:
            print("Значение скорости введено некорректно.")

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police) 

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police) 

    def show_speed(self):
        try:
            if int(self.speed) > 40:
                print(f"Скорость равна {self.speed}, она превышена!")
            else:
                print(f"Скорость равна {self.speed}")
        except:
            print("Значение скорости введено некорректно.")

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police) 

town_car = TownCar(20, "синий", "Лада, которая баклажан", False)
sport_car = SportCar(120, "белый", "GTX 3080 Ti", False)
work_car = WorkCar(140, "красный", "Xnj-nj", False)
police_car = PoliceCar(20, "черный", "Мусоровозка RX120", False)

work_car.show_speed()
town_car.show_speed()
town_car.go()
town_car.turn("право")