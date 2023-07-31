# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# 📌 У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО 
# и т.п. на ваш выбор.
# 📌 Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.

class Persona:

    def __init__(self, f_name: str, l_name: str, age: int, city: str):
        self.f_name = f_name
        self.l_name = l_name
        self._age = age
        self.city = city

    def _birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def full_name(self):
        return self.f_name + " " + self.l_name
    
    def user_city(self):
        return self.city


person1 = Persona("Ivan", "Ivanov", 37, "Moscow")
print(f'Возраст = {person1.get_age()}')
print(person1.full_name())
print(person1.city)
person1._birthday()
print(f'Возраст = {person1.get_age()}')