# a = 5
# print(type(a), id(a)) # <class 'int'> 4379904608
# a = 'hello world'
# print(type(a), id(a)) # <class 'str'> 4353701808
# a = 456 * 21 / 2
# print(type(a), id(a)) # <class 'float'> 4352207536


# data = 42
# print(isinstance(data, int))
# data = True
# print(isinstance(data, int))
# data = 3.14
# print(isinstance(data, (int, float, complex)))


# num = 2 + 2 * 2
# digit = 36 / 6
# print(num == digit) # True
# print(num is digit) # False  # is Сравнивает пару объектов на идентичность


# a = 5
# print(a, id(a))
# a += 1 # won't replace the previous value of a, but will create a new object
# print(a, id(a))


# txt = 'Hello World!'
# txt[5] = '_' # trying to change the 5th element in string txt - will return an error, string types can't be changed


# txt = 'Hello World !'
# print(txt, id(txt)) # Hello World ! 4439482544
# txt = txt.replace(' ', '_')
# print(txt, id(txt)) # Hello_World_! 4439850928


# a = c = 2
# b = 3
# print(a, id(a), b, id(b), c, id(c)) # 2 4535093760 3 4535093792 2 4535093760
# a = b + c
# print(a, id(a), b, id(b), c, id(c)) # 5 4535093856 3 4535093792 2 4535093760


# Хэш как проверка на неизменяемость
# x = 42
# y = 'text'
# z = 3.1427
# print(hash(x), hash(y), hash(z)) # 42 1578070650926561041 329043797414794243
# my_list = [x, y, z]
# print(hash(my_list)) # error - unhashable type: 'list'


# Напишите небольшую программу, которая запрашивает у пользователя любой текст и выводит о нём следующую информацию:
# ✔ тип объекта,
# ✔ адрес объекта в оперативной памяти,
# ✔ хеш объекта.
# txt = str(input("Enter your text"))
# print(txt, id(txt), type(txt), hash(txt))


#### Аннотация типов ####
# a: int = 42
# b: float = float(input("Enter your number :"))
# a = a / b # will turn value of a into float
# print(a, type(a)) # 6.0 <class 'float'>

# a: int | float = 42 # can be either int OR float
# b: float = float(input("Enter your number :"))
# a = a / b
# print(a, type(a)) # 6.0 <class 'float'>

# def my_func(data: list[int, float]) -> float: #can state what type of data you expect to input and what type to return
#     res = sum(data) / len(data)
#     return res
# print(my_func([2, 5.5, 15, 8.0, 13.74]))

# def my_func(data): # works as well, but we don't regulate the data types at input / output
#     res = sum(data) / len(data)
#     return res
# print(my_func([2, 5.5, 15, 8.0, 13.74]))


#### Атрибуты и методы ####
# print("Hello World !".__doc__)
# print(str.__doc__)

# print("Hello World !".upper()) # HELLO WORLD !
# print("Hello World !".count('l')) # 3

#print(dir("Hello World !")) # Функция dir(object) - вернуть список допустимых атрибутов для объекта
# help(str)
# help()


# import sys
#
# STEP = 2 ** 16
# num = 1
# for _ in range(30):
#     print(sys.getsizeof(num), num)
#     num *= STEP


# num = 7_901_123_567_652
# print(num) # 7901123567652


# num = 2 ** 16 - 1
# b = bin(num) # 0b1111111111111111  преобразует целое число в двоичную строку с префиксом «0b»
# o = oct(num) # 0o177777  преобразует целое число в восьмеричную строку с префиксом «0o»
# h = hex(num) # 0xffff  преобразует целое число в строчную шестнадцатеричную строку с префиксом «0x»
# print(b, o, h)


### Логические типы #### Неявное преобразование данных к истине

# DEFAULT = 42
# num = int(input("Enter level or zero for default value :"))
# level = num or DEFAULT # if entered 0 (= False) then output will be default (42 = True)
# print(level) # if entered anything but 0 then first True (not zero) value will be printed

# name = input("What's your name ?")
# if name:  # = if True = if any name was entered ^^
#     print("Hello, " + name)
# else: # if False = no name given
#     print("Hello there, Anonymous")

# data = [0, 1, 1, 2, 3, 5, 8, 13, 21] # empty set = False, one that has some data = True
# while data:
#     print(data.pop())


#### Строки и способы их записи ####

# class str(object):
#     d = """
#         str(object='') -> str
#         str(bytes_or_buffer[, encoding[,
#         errors]]) -> str
#         ...
#         """
#     print(d)


# very_long_text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. A ab alias animi assumenda at aut ' \
#                  'commodi, consequatur cumque ea harum, hic id illum ipsam itaque laboriosam magnam minus nam nulla ' \
#                  'numquam obcaecati officia officiis porro possimus praesentium quaerat temporibus ullam veniam? '
# print(very_long_text) # \ used to break up long code lines, but in the output it'll still be a one long line


#### Конкатенация строк ####

# LIMIT = 120
# ATTENTION = 'Внимание!'
# name = input('Твоё имя? ')
# age = int(input('Твой возраст? '))
# text = ATTENTION + ' Хоть тебе и осталось ' + str(100 - age) +\
#        " до ста лет, но длинна строки не должна превышать " + str(LIMIT) + ' символов'
# print(text) # all objects used in CONCAT have to be strings


#### Математические модули ####

# import fractions  # Запись дробей вида 1⁄3, 3⁄5 и т.п.
#
# f1 = fractions.Fraction(1, 3)
# print(f1)
# f2 = fractions.Fraction(3, 5)
# print(f2)
# print(f1 * f2)


# x = -42
# print(abs(x)) # 42 # abs(x) — возвращает абсолютное значение числа x, число по модулю.
#
# a = 42
# b = 5
# print(divmod(a, b)) # (8, 2)
# #  ^^ возвращает пару чисел — частное и остаток от целочисленного деления. Аналогично вычислению a // b и a % b.
#
# print(pow(a, b)) # 130691232  # pow(base, exp[, mod]) — при передаче 2-х аргументов возводит base в степень exp.
# print(pow(a, b, 10)) # 2  #При передаче 3х аргументов результат возведения в степень делится по модулю на значение mod
#
# print(round(3.141_592_653_589_793, 3)) # 3.142

