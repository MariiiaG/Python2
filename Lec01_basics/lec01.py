# name = 'Maria'
# age = None
#
# a = 42
# print(id(a)) # returns a unique identification value of the object stored in the memory
# a = 'Hello world'
# print(id(a))
#
# print(name, age, a, 456, 'text', sep=' (=^.^=) ', end='#\n') # Maria (=^.^=) None (=^.^=) Hello world (=^.^=) 456 (=^.^=) text#
# print('any text') # any text
#
# res = input('Print your text :') # no matter what, the data will be stored as String, even if it's numbers
# print('You said : ', res)
#
# age = int(input('How old are you ? ')) # int converts input data into int
# print(age + 4) # no error as it has been converted into int


# number_pi = float(input('First 3 numbers of pi : ')) #stores input data as float
# print(number_pi)
# print(number_pi + 0.06)


# pwd = 'text'
# res = input('Enter the password : ')
# if res == pwd:
#     print('Access granted')
# else :
#     print('Access denied')
# print('Logging out')


# pwd = 'text'
# res = input('Enter the password : ')
# if res == pwd:
#     print('Access granted')
#     trick_question = int(input('2 + 2 = '))
#     if 2 + 2 == trick_question :
#         print('Well done')
#     else :
#         print('Go back to school')
# else :
#     print('Access denied')
# print('Logging out')


# colour = input("What's your favourite colour ?")
# if colour == 'red' :
#     print("it's a classic ! ")
# elif colour == 'green' :
#     print('I love nature and colour green too !! ')
# elif colour == 'blue' :
#     print('How about a trip to the seaside ??')
# else :
#     print("I didn't peg you as a ", colour, ' person !')


# colour = input("What's your favourite colour ?")
# match colour:
#     case 'red' | 'black':
#         print("it's a classic ! ")
#     case 'green':
#         print('I love nature and colour green too !! ')
#     case 'blue' | 'turquoise':
#         print('How about a trip to the seaside ??')
#     case _:
#         print("I didn't peg you as a ", colour, ' person !')


# year = int(input("Enter year as yyyy : "))
# if year % 4 != 0:
#     print("Non-leap")
# elif year % 100 == 0:
#     if year % 400 == 0:
#         print("It's a leap year !! ")
#     else:
#         print('Non-leap year')
# else:
#     print("It's a leap year !! ")


# year = int(input("Enter year as yyyy : "))
# if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
#     print("Non-leap")
# else:
#     print("It's a leap year !! ")


# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]  # Проверка на вхождение
# num = int(input('Enter an int number : '))
# if num in data:  # if num not in data   <-- to do the opposite
#     print("Well done ! It's in the Fibonacci sequence")


# my_math = int(input('2 + 2 = '))  # Тернарный оператор - Сокращённая запись if-else в одну строку
# print('Bingo !' if 2 + 2 == my_math else 'You sure ?')


# Логический цикл while
# num = float(input('Enter your number : '))
# count = 0
# while count < num:
#     print(count)
#     count += 2 # can use other math functions here:  num //= 2   num *= 2  ....


# num = float(input('Enter your number : '))
# STEP = 2
# limit = num - STEP
# count = -STEP
# while count < limit:
#     count += STEP
#     if count % 12 == 0: # will skip and not print the result when count = 12
#         continue
#     print(count)


# min_limit = 0
# max_limit = 10
# while True:
#     print('Enter a number between', min_limit, 'and', max_limit, ':')
#     num = float(input())
#     if num < min_limit or num > max_limit:
#         print('Input error')
#     else:
#         break # the loop will only break when the statement in 'while true' becomes false
# print('You entered ', num)


# min_limit = 0
# max_limit = 10
# count = 3
# num = None
#
# while count > 0:
#     print('Attempt #', count)
#     count -= 1
#
#     print('Enter a number between', min_limit, 'and', max_limit, ':')
#     num = float(input())
#     if num < min_limit or num > max_limit:
#         print('Input error')
#     else:
#         break
#
# else:
#     print("You've maxed out your attempts, sorry")
#     quit()
#
# print('Input number is', num)


# Цикл итератор for in
# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# for item in data:
#     print(item)
#
# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# for _ in data:
#     print("Hello") # prints "Hello" for each item in the array - 9 x Hello in this case

# num = int(input("Enter a number :")) # range only accepts integers !!
# for i in range(0, num, 2): # range(start, stop, step) value for 'stop' is not inclusive
#     print(i)

# animals = ['cat', 'dog', 'wolf', 'rat', 'dragon']
# for i, animal in enumerate(animals, start=1):
#     print(i, animal) # 1 cat / 2 dog / 3 wolf / ... in a column


# data = 0
# while data < 100:
#     data += 2
#     if data % 40 == 0:
#         break
# print(data) # 40

# data = 0
# while data < 100:
#     data += 3
#     if data % 19 == 0:
#         continue # if data % 19 == 0 the loop will skip everything below and continue at 'while' clause
#     data += 1
#     if data % 40 == 0:
#         break
# else:
#     data += 5
# print(data) # 80