# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

import random

class Fish():
    def __init__(self, name: str, age: int, areal: str):
        self.name = name
        self.age = age
        self.areal = areal

    def say(self):
        print("буль-буль")

    def eat(self):
        print("ням-ням")

    def child(self):
        a = list(self.name)
        random.shuffle(a)
        a = "".join(a)
        return Fish(a, 0, self.areal)


class Bird():
    def __init__(self, name: str, age: int, size_wings: int):
        self.name = name
        self.age = age
        self.size_wings = size_wings

    def wings(self):
        if self.size_wings > 100:
            print("Это большая птица")
        else:
            print("Это маленькая птичка")

    def say(self):
        print("чик-чирик")

    def eat(self):
        print("ням-ням")


class Fabrica:
    def create_animal(self, animal_type: str, *args, **kwargs):
        if animal_type == 'fish':
            new_animal = Fish(*args, **kwargs)
            return new_animal
        elif animal_type == 'bird':
            new_animal = Bird(*args, **kwargs)
            return new_animal
        else:
            print('Такое животное создать не могу')
            exit()


if __name__ == '__main__':
    
    fabrica = Fabrica()
    new_animal = fabrica.create_animal("fish", "Fishka", 5, "river")
    new_animal.say()
    new_animal.eat()