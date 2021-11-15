# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, email. Функция должна принимать параметры
# как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
def user_data(name, surname, date, city, email, phone):
    print(f"{name} {surname} {date} {city} {email} {phone}")


name = input("Введите имя: ")
surname = input("Введите фамилию: ")
date = input("Введите год рождения: ")
city = input("Введите город проживания: ")
email = input("Введите email: ")
phone = input("Введите телефон: ")
user_data(name=name, surname=surname, date=date, city=city, email=email, phone=phone)