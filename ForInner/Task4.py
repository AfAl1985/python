print("Задание 4. Простые числа")
# Что нужно сделать
# Напишите программу, которая считает количество простых чисел
# в заданной последовательности и выводит ответ на экран.
# Простое число делится только на себя и на единицу.
# Последовательность задаётся при помощи вызова ввода (input)
# на каждой итерации цикла. Одна итерация — одно число.
# Пример:
# Введите количество чисел: 6.
# Введите число: 4.
# Введите число: 7.
# Введите число: 20.
# Введите число: 3.
# Введите число: 11.
# Введите число: 37.
# Количество простых чисел в последовательности: 4.
# Рекомендации по выполнению
# Простое число имеет только два делителя, поэтому для проверки нужно
# перебрать все числа от одного до него.
# Если загаданное число делится без остатка на что-то,
# кроме единицы или себя, то это уже не простое число.
# Важно учесть, что минимальный делитель числа
# никогда не превышает квадратный корень из этого числа.
# Не нашли у N делителей от числа 2 до квадратного корня из N включительно? Значит, уже и не найдёте и число — простое. Это существенно ускоряет нахождение простых чисел.

numbers = int(input("Enter the number of digits: "))
count = 0

for line in range(numbers):
    result = int(input("Enter a number: "))
    for i in range(2, result):
        if result % i == 0:
            break
    else:
        count += 1
print(count)