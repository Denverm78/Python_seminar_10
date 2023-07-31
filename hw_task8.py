# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали. 
# Превратите функции в методы класса, а параметры в свойства. 
# Задачи должны решаться через вызов методов экземпляра.


import json

class Users:
    
    def __init__(self, user_name: str, user_id: str, user_level: int):
        self.user_name = user_name
        self.user_id = user_id
        self.user_level = user_level
        

    def create_users_json(self):
        with open('date_users.json', 'r', encoding='utf-8') as d_u:
            dict_levels = json.load(d_u)
        values_list = []
        for value in dict_levels.values():
            for key in value:
                values_list.append(key)
        if self.user_id not in values_list:
            dict_users = dict_levels[self.user_level]
            dict_users[self.user_id] = self.user_name
            dict_levels[self.user_level] = dict_users
        else:    
            print("Такой id уже существует")
            
                    
        with open('date_users.json', 'w', encoding='utf-8') as f:
            json.dump(dict_levels, f, indent=2, ensure_ascii=False)
            
if __name__ == '__main__':
    
    MIN_LEVEL = 1
    MAX_LEVEL = 7
    while True:
        user_name = input("Введите имя пользователя: ")
        user_id = input("Введите личный идентификатор: ")
        user_level = input(f"Введите уровень доступа от {MIN_LEVEL} до {MAX_LEVEL}: ")
        
        create_new_user = Users(user_name, user_id, user_level)
        create_new_user.create_users_json()               

    