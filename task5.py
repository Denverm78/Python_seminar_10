# Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# 📌 У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# 📌 Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

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


class Birds():
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
        
        
fish1 = Fish("karl", 2, "ocean")
fish1.say()
fish1.eat()
fish2 = fish1.child()
fish2.say()
fish2.eat()
bird1 = Birds("chig", 2, 105)
bird1.wings()
bird1.say()
print(bird1.name)      