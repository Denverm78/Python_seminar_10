# Создайте класс прямоугольник.
# 📌 Класс должен принимать длину и ширину при создании экземпляра.
# 📌 У класса должно быть два метода, возвращающие периметр и площадь.
# 📌 Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

class Rectangle:
    def __init__(self, a, b=None):
        if b == None:
            b = a
        self.a = a
        self.b = b

    def perimeter(self):
        return (self.a + self.b) * 2

    def sq(self):
        return self.a * self.b


rec = Rectangle(10, 5)
print('Сторона a = ', rec.a)
print('Сторона b = ', rec.b)
print('Периметр = ', rec.perimeter())
print('Площадь = ', rec.sq())