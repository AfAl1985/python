print("Задание 6. Пирамидка")
# Что нужно сделать
# Напишите программу, которая выводит на экран равнобедренный треугольник
# (пирамидку), заполненный символами хештега (#).
# Пусть высоту пирамиды определяет пользователь.
    #
   ###
  #####
 #######
# Что оценивается
# Советы и рекомендации
# Вспомните, как выводился колонтитул вида -----!!!!!!-----.
# Не забывайте, что для нас пробел — это пустое место,
# а для Python — это такой же символ, как и любой другой.
# Если нужно добавить отступ, необходимо использовать пробел
# или символ табуляции (\t).

height = int(input("enter a height ot triangle: "))

for row in range(1, height + 1):
    print(' ' * (height - row), '#' * ((row * 2) - 1))



