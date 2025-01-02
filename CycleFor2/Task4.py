print("Задача 4. Среднее на отрезке")
# Что нужно сделать
# Напишите программу, которая считывает с клавиатуры три числа a, b и c,
# считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу c.
#
# Рекомендации
# Функция range(start, stop) не включает границу stop, останавливается, не доходя до неё.

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))
summ = 0
count = 0

for line in range(first, second + 1):
    if (line % third == 0):
        print(line)
        count += 1
        summ += line
print(summ / count)

