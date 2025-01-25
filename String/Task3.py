print('Задание 3. Театр')
# В городе планируют построить театр под открытым небом,
# но для начала нужно оценить, сколько сделать рядов,
# сидений в них и каким должно быть расстояние между рядами.
#
# Что нужно сделать
# Напишите программу, которая получает на вход количество рядов,
# сидений и свободных метров между рядами, а затем выводит примерный макет театра на экран.
# Enter the number of raws: 5
# Enter the number of seats in a raw: 7
# Enter the length between raws: 3
#
# Scene
# ===== *** =====
# ===== *** =====
# ===== *** =====
# ===== *** =====
# ===== *** =====

rows = int(input("Enter the number of raws: "))
seats = int(input("Enter the number of seats: "))
length = int(input("Enter the length between the raws: "))

print("Scene")
for line in range (rows):
    print()
    print('=' * seats, '*' * length, '=' * seats, end= '')