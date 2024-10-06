# Напишите функцию get_multiplied_digits и параметр number в ней.
def get_multiplied_digits(number):
    # Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
    str_number = str(number)
    # Создайте переменную first и запишите в неё первый символ из str_number в числовом представлении(int).
    first = int(str_number[0])
    # Если длина str_number больше 1, тогда вернуть значение first * get_multiplied_digits(int(str_number[1:])).
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    # Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first.
    else:
        return int(first)

# Вывод на консоль:
result = get_multiplied_digits(40203)
print(result) # 24