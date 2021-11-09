def int_func(text):
    word = text[0].upper() + text[1:].lower()
    return word


str = input("Введи слова через пробел: ")
for word in str.split(' '):
    print(f'{int_func(word)} ', end=' ')

