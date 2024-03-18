# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

balance = 5400000
count_a = 0
count_o = 0

while True:
    if balance > 5_000_000:
        print(f"Wealth tax {balance * 0.1}")
        balance -= balance * 0.1
    action = input("Enter your command :")
    if action == 'q':
        print(f"Available balance : {balance}")
        print("Logging off")
        break
    elif action == 'a':
        amount = int(input("Enter deposit amount :"))
        if amount % 50 == 0:
            balance += amount
            count_a += 1
            if count_a % 3 == 0:
                balance *= 1.03
        else:
            print("Incorrect amount")
    elif action == 'o':
        amount = int(input("Enter withdrawal amount : "))
        fee = amount * 0.015
        if fee < 30:
            fee = 30
        elif fee > 600:
            fee = 600
        if amount + fee > balance:
            print("Insufficient funds")
        else:
            if amount % 50 == 0:
                balance -= amount + fee
                count_o += 1
                if count_o % 3 == 0:
                    balance *= 1.03
            else:
                print("Incorrect amount")

    print(f'Available balance : {balance}')
