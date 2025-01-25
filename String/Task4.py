print('Задание 4. Марсоход-2')
# К роботу Валли отправили «коллегу» Билли.
# Это его первая высадка на Марс, поэтому его тестируют в прямоугольном помещении размером 15 × 20 м.
# Марсоход высаживается в центре комнаты (в точке 8, 10), затем управление им передаётся оператору,
# то есть пользователю вашей программы.
# Программа спрашивает, в какую сторону оператор хочет направить робота: север (клавиша W),
# юг (клавиша S), запад (клавиша A) или восток (клавиша D).
# Оператор делает выбор, марсоход перемещается в эту сторону на один метр,
# а программа сообщает новую позицию робота. Если марсоход упёрся в стену,
# он не должен пытаться переместиться в сторону стены — в этом случае его позиция не меняется.
# Что нужно сделать
# Создайте программу для управления роботом Билли.
# Пример:
# [Программа]: Марсоход находится на позиции 6, 19, введите команду:
# [Оператор]: A
# [Программа]: Марсоход находится на позиции 5, 19, введите команду:
# [Оператор]: W
# [Программа]: Марсоход находится на позиции 5, 20, введите команду:
# [Оператор]: W
# [Программа]: Марсоход находится на позиции 5, 20, введите команду:

x = 8
y = 10
print("The Mars observer on the position: ", x, y)

while True:
    coordinates = input("Enter the destination W A S D: ")
    if coordinates == 'W' and x != 0:
        x -= 1
    elif coordinates == 'S' and x != 15:
        x += 1
    elif coordinates == 'A' and y != 0:
        y -= 1
    elif coordinates == 'D' and y != 20:
        y += 1
    else:
        break
    print(x, y)
print(x, y)



