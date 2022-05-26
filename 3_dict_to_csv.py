"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv 

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    with open('users.csv', 'r', encoding='utf-8') as f:
        fields = ['name', 'age', 'job']
        reader = csv.DictReader(f, fields, delimiter=';')
        for row in reader:
            print(row)

    users_name =  [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        {'name': 'Настя', 'age': 31, 'job': 'Manager'}
    ]

    with open('user3.csv','w', encoding='utf-8') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=";")
        writer.writeheader()
        for user in users_name:
            writer.writerow(user)



if __name__ == "__main__":
    main()
