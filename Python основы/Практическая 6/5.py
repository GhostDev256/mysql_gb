# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Рисую что-то карандашом.")

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Рисую что-то маркером.")

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Рисую что-то ручкой.")

pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")

pen2 = Stationery("Цветной карандаш")

pen2.draw()
pen.draw()
pencil.draw()
handle.draw()