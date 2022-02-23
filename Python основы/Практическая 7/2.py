# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, 
# которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды 
# существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# 
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). 
# Проверить работу этих методов на реальных данных.

# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать 
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Fabrics:
    def __init__(self, width, height):
        self.width = width
        self.height = height 

    def square_coat(self):
        return f"Площадь на пальто: {(self.width / 6.5) + 0.5}"

    def square_suit(self):
        return f"Площадь на костюм: {(self.height * 2) + 0.3}"

    @property
    def full(self):
        return f"Общая площадь ткани: {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}"

class Coat(Fabrics):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f"Площадь на пальто: {self.square_c}"

class Suit(Fabrics):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_s = round(self.height * 2 + 0.3)

    def __str__(self):
        return f"Площадь на костюм: {self.square_s}"

coat = Coat(6, 12)
suit = Suit(24, 48)

print(coat, "; ", suit)
print(coat.full, "; ", suit.full)

print(suit.square_coat())
print(suit.square_suit())