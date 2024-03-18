# ✔ Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять не менее 42 знаков после запятой.

import decimal
import math


def area(d):
    decimal.getcontext().prec = 42
    pi = decimal.Decimal(str(math.pi))
    d = decimal.Decimal(str(d))
    return pi * (d / 2) ** 2


def len_circle(d):
    decimal.getcontext().prec = 42
    pi = decimal.Decimal(str(math.pi))
    d = decimal.Decimal(str(d))
    return pi * d


print(area(12))
print(len_circle(12))
