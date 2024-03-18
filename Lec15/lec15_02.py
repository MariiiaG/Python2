import argparse

parser = argparse.ArgumentParser(description="Вводим стоимость обеда и процент чаевых")
parser.add_argument('-price', type=int, default=100)
parser.add_argument('-tip', type=int, default=15)

args = parser.parse_args()
print(args)

def calc_cost(price, tip):
    return price + price * tip / 100


print(calc_cost(1000, 15))