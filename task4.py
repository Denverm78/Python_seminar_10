# Создайте класс Сотрудник.
# 📌 Воспользуйтесь классом человека из прошлого задания.
# 📌 У сотрудника должен быть: 
# ○ шестизначный идентификационный номер 
# ○ уровень доступа, вычисляемый как остаток от деления суммы цифр id на семь

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


class Employer(Persona):
    def __init__(self, f_name: str, l_name: str, age: int, city: str, id: int):
        self.id = id
        super().__init__(f_name, l_name, age, city)

    def level(self):
        return sum(int(num) for num in str(self.id)) % 7


empl = Employer("Lilia", " Sorokina", 30, "Moscow", 512647)
print(f'Возраст = {empl.get_age()}')
print(empl.full_name())
print(empl.level())