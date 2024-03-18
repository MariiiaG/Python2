# Нарисовать в консоли ёлку, спросив у пользователя количество рядов
# Пример : 5
#      *
#     ***
#    *****
#   *******
#  *********

steps = 5
figure = '*'
space = ' '
num_figure = 1
num_space = steps -1
for _ in range(steps):
    print((space * num_space) + (figure * num_figure) + (space * num_space))
    num_figure += 2
    num_space -= 1
