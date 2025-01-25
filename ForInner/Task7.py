print("Задание 7. Пирамидка-2")
# Что нужно сделать
# Напишите программу, которая получает на вход количество уровней пирамиды
# и выводит их на экран, заполняя нечётными числами:
#        1
#      3   5
#     7   9   11
#   13  15  17  19
# 21  23  25  27  29
height = int(input("Enter a height of a piramyd: "))
num = 1
# for row in range(1, height + 1):
#     print('\t' * (height - row), end= '')
#     for col in range(row):
#         print(num, end= '')
#         num += 2
#         print('\t' * 2, end= '')
#     print()

for line in range(height):
    space = height - line - 1
    print('   ' * space, end= '')
    for number in range(line + 1):
        print(num, end= '    ')
        num += 2
    print()
