print('Задача 3. Успеваемость в классе')

# В классе N человек. Каждый из них получил за урок по информатике три, четыре или пять, двоек сегодня не было.

# Напишите программу, которая получает список оценок — N чисел
# — и выводит на экран сообщение о том, кого сегодня больше: отличников, хорошистов или троечников.
# Замечание: можно предположить, что количество отличников, хорошистов и троечников различно.

# Пример
# Сколько в классе учеников? 5
# Введите оценку ученика: 3
# Введите оценку ученика: 4
# Введите оценку ученика: 4
# Введите оценку ученика: 5
# Введите оценку ученика: 4
# Сегодня больше хорошистов!

students = int(input("Enter a number of students:"))
excellent = 0
good = 0
satisfactory = 0
count_excellent = 0
count_good = 0
count_satisfactory = 0

for mark in range(students):
    mark = int(input("Enter the grade: "))
    if mark == 5:
        excellent += 1
        count_excellent += 1
    elif mark == 4:
        good += 1
        count_good += 1
    else:
        satisfactory += 1
        count_satisfactory += 1
print("number of excellent: ",count_excellent)
print("number of good: ",count_good)
print("number of satisfactory: ",count_satisfactory)
if excellent > good and excellent > satisfactory:
    print("More excellent students")
elif good > excellent and good > satisfactory:
    print("More good students")
else:
    print("More satisfacoty students")


