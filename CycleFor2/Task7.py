print("Задача 7. Сумма ряда")
# Что нужно сделать
# Дано натуральное число N. Напишите программу для вычисления суммы
# N элементов последовательности по формуле (-1) ** n * 1/2 ** n
# где n — это порядковый номер элемента (расчёт начинается с нуля).
# Примеры расчётов
# При N = 4 элементы выражения будут равны:
# n = 0
# elem = (−1) ** 0 * (½) ** 0 = 1
# n = 1
# elem = (−1) ** 1 * (½) ** 1 = (−½)
# n = 2
# elem = (−1) ** 2 * (½) ** 2 = ¼
# n = 3
# elem = (−1) ** 3 * (½) ** 3 = (−⅛)
# Сумма равна:
# s = 1 - 1/2 + 1/4 - 1/8 = 5/8 = 0,625
# При N = 6 элементы выражения будут равны:
# n = 0
# elem = (−1) ** 0 * (½) ** 0 = 1
# n = 1
# elem = (−1) ** 1 * (½) ** 1 = (−½)
# n = 2
# elem = (−1) ** 2 * (½) ** 2 = ¼
# n = 3
# elem = (−1) ** 3 * (½) ** 3 = (−⅛)
# n = 4
# elem = (−1) ** 4 * (½) ** 4 = (1/16)
# n = 5
# elem = (−1) ** 5 * (½) ** 5 = (−1/32)
# Сумма равна:
# s = 1 − ½ + ¼ − ⅛ + 1/16 − 1/32 = 21/32 = 0,65625
# P. S. Не стоит выполнять расчёты каждого элемента вручную, используйте цикл.
# Примеры вывода в консоль
# Введите N: 4
# Ответ: 0,625
# Введите N: 6
# Ответ: 0,65625

number = int(input("Enter the number: "))
s = 0

for line in range(0, number, 1):
    s = s + (-1) ** line * 1/(2**line)
print(s)