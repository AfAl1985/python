print("Задание 3. Рамка")
# Что нужно сделать
# Напишите программу, которая рисует прямоугольную рамку
# с помощью символьной графики.
# Для вертикальных линий используйте символ вертикального штриха (|),
# а для горизонтальных — дефис (-). Пусть ширину и высоту рамки
# определяет пользователь.
# |-------------|
# |             |
# |             |
# |             |
# |             |
# |-------------|
for row in range(10):
    for col in range(20):
        if col == 0 or col == 19:
            print("|", end= '')
        elif row == 0 or row == 9:
            print("-", end='')
        else:
            print(" ", end= '')
    print()

