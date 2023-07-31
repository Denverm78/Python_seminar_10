# Доработайте задачу 5.
# 📌 Вынесите общие свойства и методы классов в класс Животное.
# 📌 Остальные классы наследуйте от него.
# 📌 Убедитесь, что в созданные ранее классы внесены правки.

import random

class Animals:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def _birthday(self):
        self.age += 1


class Fish(Animals):
    def __init__(self, name: str, age: int, areal: str):
        self.areal = areal
        super().__init__(name, age)

    def say(self):
        print("буль-буль")

    def eat(self):
        print("ням-ням")

    def child(self):
        a = list(self.name)
        random.shuffle(a)
        a = "".join(a)
        return Fish(a, 0, self.areal)


class Birds(Animals):
    def __init__(self, name: str, age: int, size_wings: int):
        self.size_wings = size_wings
        super().__init__(name, age)

    def wings(self):
        if self.size_wings > 100:
            print("Это большая птица")
        else:
            print("Это маленькая птичка")

    def say(self):
        print("чик-чирик")

    def eat(self):
        print("ням-ням")


fish1 = Fish("karl", 2, "ocean")
fish1.say()
fish1.eat()
print(fish1.get_age())
print(fish1.get_name())
fish2 = fish1.child()
fish2.say()
fish2.eat()
print(fish2.get_age())
print(fish2.get_name())
bird1 = Birds("Chig", 2, 105)
bird1.wings()
bird1.say()
print(bird1.name)
