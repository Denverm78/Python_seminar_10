# Создайте класс окружность.
# 📌 Класс должен принимать радиус окружности при создании экземпляра.
# 📌 У класса должно быть два метода, возвращающие длину окружности и её площадь.


class Circle:
    def __init__(self, radius):
        self.r = radius

    def len(self):
        return 2 * 3.14 * self.r

    def sq(self):
        return 3.14 * self.r ** 2


crc = Circle(10)
print('Радиус окружности = ', crc.r)
print('Длина окружности = ', round(crc.len(), 2))
print('Площадь окружности = ', crc.sq())