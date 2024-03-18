# list_1 = list()
# list_2 = list((3.14, True, "Hello world!"))
# list_3 = []
# list_4 = [3.14, True, "Hello world!"]
# print(list_1, list_2, list_3, list_4) # [] [3.14, True, 'Hello world!'] [] [3.14, True, 'Hello world!']
# print(list_1.__sizeof__(), list_2.__sizeof__(), list_3.__sizeof__(), list_4.__sizeof__()) # 40 72 40 72


### Обращение к элементам списка по индексу ###
#
# my_list = [2, 4, 6, 8, 10, 12]
# print(my_list[0]) # 2
# #print(my_list[6]) # IndexError: list index out of range
#
# print(my_list[-1]) # 12
# print(my_list[--2]) # 6
# #print(my_list[-10]) # IndexError: list index out of range


### Append ###
#
# a = 42
# b = 'Hello world!'
# c = [1, 3, 5, 7]
# my_list = [None]
# my_list.append(a)
# print(my_list) # [None, 42]
# my_list.append(b)
# print(my_list) # [None, 42, 'Hello world!']
# my_list.append(c)
# print(my_list) # [None, 42, 'Hello world!', [1, 3, 5, 7]]


### Extend ### В качестве аргумента extend принимает последовательность, итерируется по ней слева направо
# и каждый элемент добавляет в новую ячейку списка
#
# a = 42
# b = 'Hello world!'
# c = [1, 3, 5, 7]
# my_list = [None]
# #my_list.extend(a) # TypeError: 'int' object is not iterable print(my_list) # передали не коллекцию
# my_list.extend(b)
# print(my_list)
# my_list.extend(c)
# print(my_list)
# my_list.extend(my_list)
# print(my_list) # удваиваем список, добавляя копию всех его элементов.


### Метод Pop - позволяет удалить элемент списка. Удаляемый элемент возвращается как результат работы метода.
#
# my_list = [2, 4, 6, 8, 10, 12]
# spam = my_list.pop()
# print(spam, my_list) # 12 [2, 4, 6, 8, 10]
# eggs = my_list.pop(1)
# print(eggs, my_list) # 4 [2, 6, 8, 10]
# #err = my_list.pop(10) # IndexError: pop index out of range


### Метод count - подсчитывает вхождение элемента в список. Принимает именно объект, а не индекс.
#
# my_list=[2,4,6,2,8,10,12,2,4,14,2]
# spam = my_list.count(2) # 4
# print(spam)
# eggs = my_list.count(3) # 0
# print(eggs)


### Метод index - возвращает индекс переданного объекта внутри списка.
#
# my_list = [2, 4, 6, 2, 8, 10, 12, 2, 4, 14, 2]
# spam = my_list.index(4)
# print(spam) # 1  (работает до первого вхождения)
# eggs = my_list.index(4, spam + 1, 90) # индекс start и индекс stop - поиск внутри диапазона
# print(eggs) # 8
# #err = my_list.index(3) # ValueError: 3 is not in list


### Метод insert - принимает два аргумента — индекс для вставки и объект вставки. Добавляет элемент после индекса.
#
# my_list = [2, 4, 6, 8, 10, 12]
# print(my_list)
# my_list.insert(2, 555) # 2 = встанет НА ВТОРУЮ позицию
# print(my_list) # [2, 4, 555, 6, 8, 10, 12]
# my_list.insert(-2, 13)  # -2 = встанет ПОСЛЕ ВТОРОЙ позиции с конца
# print(my_list) # [2, 4, 555, 6, 8, 13, 10, 12]
# my_list.insert(42, 73) # my_list.append(73)  // индекс больше - добавляется в конецю Лучше append
# print(my_list) # [2, 4, 555, 6, 8, 13, 10, 12, 73]


### Метод remove - принимает на вход объект, производит его поиск в списке и удаляет в случае нахождения.
#
# my_list = [2, 4, 6, 8, 10, 12, 6]
# print(my_list)
# my_list.remove(6) # Если элемент встречается в списке несколько раз, удаляется только самый левый.
# print(my_list) # [2, 4, 8, 10, 12, 6]
# # my_list.remove(3) # ValueError: list.remove(x): x not in list
# print(my_list) # [2, 4, 8, 10, 12, 6]


### Сортировки и развороты - При сортировке элементы списка должны быть одного типа

## Функция sorted() - принимает любую коллекцию по которой можно итерироваться и возвращает отсортированный список
#
# my_list = [4, 8, 2, 9, 1, 7, 2]
# sort_list = sorted(my_list) # [1, 2, 2, 4, 7, 8, 9]
# print(my_list, sort_list, sep='\n') # Переданная в функцию коллекция остаётся неизменной
# rev_list = sorted(my_list, reverse=True) # [9, 8, 7, 4, 2, 2, 1]
# print(my_list, rev_list, sep='\n')

## Метод sort() - осуществляет сортировку элементов списка без создания копии, inplace.
#
# my_list = [4, 8, 2, 9, 1, 7, 2]
# my_list.sort()
# print(my_list) # [1, 2, 2, 4, 7, 8, 9]
# my_list.sort(reverse=True)
# print(my_list) # [9, 8, 7, 4, 2, 2, 1]

## Функция reversed()- принимает последовательность, которая поддерживает порядок элементов,
# возвращает функция объект итератор с обратным порядком элементов.
# Если нам нужен новый развёрнутый список, объект итератор стоит обернуть в функцию list
#
# my_list=[4,8,2,9,1,7,2]
# res = reversed(my_list)
# print(type(res), res) # <class 'list_reverseiterator'> <list_reverseiterator object at 0x102ca32b0>
# rev_list = list(reversed(my_list)) # [2, 7, 1, 9, 2, 8, 4]
# print(rev_list)

## Метод reverse() - развёрнутая версия списка, логичные и удобнее использовать
#
# my_list = [4, 8, 2, 9, 1, 7, 2]
# my_list.reverse() # разворачивает список на месте не создавая копии
# print(my_list) # [2, 7, 1, 9, 2, 8, 4]

# my_list = [4, 8, 2, 9, 1, 7, 2]
# new_list = my_list[::-1] # получить развернутую копию
# print(my_list, new_list, sep='\n') # [2, 7, 1, 9, 2, 8, 4]


## Срезы - Используя квадратные скобки можно делать частичные копии списка - срезы.
# Базовый синтаксис   list[start:stop:step]

# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# print(my_list[2:7:2]) # [6, 8, 12]
# print(my_list[:7:2]) # [2, 6, 8, 12]
# print(my_list[2::2]) # [6, 8, 12, 16]
# print(my_list[2:7:]) # [6, 2, 8, 10, 12]
# print(my_list[8:3:-1]) # [16, 14, 12, 10, 8]
# print(my_list[3::]) # [2, 8, 10, 12, 14, 16, 18]
# print(my_list[:7:]) # [2, 4, 6, 2, 8, 10, 12]


## Метод copy() - создаёт поверхностную копию списка.
#
# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# new_list = my_list
# print(my_list, new_list, sep='\n') # [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# my_list[2] = 555 # поменяет элемент в обоих списках
# print(my_list, new_list, sep='\n') # [2, 4, 555, 2, 8, 10, 12, 14, 16, 18]

# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# new_list = my_list.copy()
# print(my_list, new_list, sep='\n') # [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# my_list[2] = 555
# print(my_list, new_list, sep='\n') # [2, 4, 555, 2, 8, 10, 12, 14, 16, 18]  [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]

### copy.deepcopy() для работы с вложенными друг в друга коллекциями. Например матрица или список списков.
#
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new_m = matrix.copy()
# print(matrix, new_m, sep='\n') # same [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix[0][1] = 555 # will change both
# print(matrix, new_m, sep='\n') # same [[1, 555, 3], [4, 5, 6], [7, 8, 9]]

# import copy
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new_m = copy.deepcopy(matrix) # для создания полной копии любой глубины вложенности
# print(matrix, new_m, sep='\n') # same [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix[0][1] = 555
# print(matrix, new_m, sep='\n') # [[1, 555, 3], [4, 5, 6], [7, 8, 9]]  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]





