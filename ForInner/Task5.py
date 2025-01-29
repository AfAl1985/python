print("Задание 5. Наибольшая сумма цифр")
# Что нужно сделать
# Пользователь вводит N чисел. Среди натуральных чисел,
# которые он указал, найдите наибольшее по сумме цифр.
# Выведите на экран это число и сумму его цифр.

numbers = int(input("Enter a number of digits: "))
maxNumber = 0
maxSum = 0
for line in range(numbers):
    num = int(input("Enter a number: "))
    maxNumber = num
    summ = 0
    while num != 0:
        summ = summ + (num % 10)
        num //= 10
        if summ > maxSum:
            maxSum = summ
            max_n = maxNumber
print("Number: ", max_n, "\t","Sum of digits: ", maxSum)
print()









