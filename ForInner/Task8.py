print("Задание 8. Яма")
# Что нужно сделать
# Представьте, что вы разрабатываете компьютерную игру с текстовой графикой.
# Вам поручили создать генератор ландшафта. Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде ямы:
# 5
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345

depth = int(input("Enter a number: "))

for row in range(depth):
    for left in range(depth, depth - row - 1, -1):
        print(left, end= '')
    point = 2 * (depth - row - 1)
    print('.' * point, end= '')
    for right in range(depth - row, depth + 1):
            print(right, end= '')
    print()
