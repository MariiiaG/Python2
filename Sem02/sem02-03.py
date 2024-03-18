# ✔ Напишите программу, которая получает целое число и возвращает его двоичное,
# восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

number = int(input("Enter your number :"))
base = int(input("enter 2 for binary or 8 for octal :"))


def convert_bin_oct(number: int, base: int) -> str:
    res = ''
    if base == 2 or base == 8:
        while number > 0:
            res = str(number % base) + res
            number = number // base
    else:
        res += "Please only enter 2 or 8"
    return res


print(convert_bin_oct(number, base))

print("===Checking===")
print(bin(number))
print(oct(number))