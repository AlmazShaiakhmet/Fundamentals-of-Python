#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def my_func(num_1, num_2, num_3):
    sum_num = num_1 + num_2 + num_3
    return sum_num - min((num_1, num_2, num_3))


a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))
z = my_func(a, b, c)
print(f"сумму наибольших двух аргументов = {z}")
