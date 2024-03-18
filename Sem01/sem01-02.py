# Посчитайте сумму четных элементов от 1 до n, исключая кратные е
# Используйте while и if
# Попробуйте разные значения е и n

n, e = 10, 3
sum_value = 0
elem = 0
while elem <= n:
    elem += 1
    if elem % 2 == 0:
        if elem % e == 0:
            continue
        sum_value += elem
print(f'Сумма = {sum_value}')
