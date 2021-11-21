# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

script_name, output_in_hours, rate_per_hour, prize = argv

print("Имя скрипта: ", script_name)
print("\n<< Программа рассчета заработной платы сотрудника >>")
print("Выработка в часах: ", output_in_hours)
print("Ставка в час: ", rate_per_hour)
print("Премия: ", prize)
print("Зарплата сотрудника: ", (float(output_in_hours) * float(rate_per_hour)) + float(prize))
