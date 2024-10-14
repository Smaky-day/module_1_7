immutable_var = (13, 4, False, 'smoky', ('s', 't', 'a', 'r'), ['h', 'o', 't'])
print(immutable_var)
# immutable_var = (13, 4, False, 'smoky')
# immutable_var[0][2] = 0   # при попытке изменить чило внутри картежа - получим TypeError,
# print(immutable_var)      # т.к. это допускается только для списка, словаря и множества

print(immutable_var[0])  # Вывести элемент можно
mutable_list = (['s', 't', 'a', 'r'], ['h', 'o', 't']) # два списка в одном картеже
mutable_list[0][3] = 'y'  # заменяем четвертый элемент первого списка
mutable_list[1][1] = 'i'  # заменяем второй элемент второго списка
print(mutable_list)       # вывод без ошибок, допустимые действия
immutable_var = tuple("stay with me") # создаем картеж: строка + функция tuple()
print(immutable_var)
immutable_var = (3.14,) # создаем картеж из одного элемента
print(immutable_var, type (immutable_var))   # картеж из одного элемента
immutable_var_1 = (2, 4, 7)
immutable_var_2 = (4, 1, 7)
print(immutable_var_1 >= immutable_var_2) # равество картежей
