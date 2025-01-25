number = int(input("Enter the frist number: "))
step = int(input("Enter the step: "))
summ = 0

print('\nIP-address: ', end= ' ')
for count in range(3):
    print(number, end= '.')
    summ += number
    number += step
print(summ)