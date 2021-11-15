"""Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные
о фирме: название, форма собственности, выручка, издержки. Необходимо вычислить
прибыль каждой компании и среднюю прибыль. Реализовать список, содержащий словарь
(название фирмы и прибыль) и словарь с одним элементом (средняя прибыль). Добавить в
первый словарь еще один элемент, содержащий результат вычисления отношения прибыли к
убыткам. Итоговый список сохранить в файл.
Подсказка: использовать менеджеры контекста."""


file = open("file_task_07.txt")
str = file.read().split("\n")
print(str)

dict_firm_profit = {}
dict_firm_profit_rent = {}

for item in str:
    key = item.split(" ")[0]
    value = item.split(" ")[2:]
    revenue = item.split(" ")[2:-1]     # выручка
    revenue = int(revenue[0])
    profit = int(value[0]) - int(value[1])  # прибыль
    rent = profit / revenue * 100  # рентабельность
    rent = int(rent)
    dict_firm_profit[key] = profit
    dict_firm_profit_rent[key] = profit, rent
print(dict_firm_profit)
