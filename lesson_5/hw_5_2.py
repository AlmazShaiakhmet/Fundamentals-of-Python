# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет
# количества строк, количества слов в каждой строке.

f = open('file_task_02.txt', 'r+')
f.truncate()
str_list = ['ветер\n', 'телевизор приставка\n', 'огурец помидор капуста баклажан\n']
f.writelines(str_list)

f = open('file_task_02.txt')
line_count = 0
for line in f:
    line_count += 1

    flag = 0
    word = 0
    for j in line:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print(line, word, 'слово')

print("Количество строк в файле: ", line_count)
f.close()
