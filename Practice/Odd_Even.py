n = int(input("Enter the number: "))
for number in range(1, n//2 + n%2 + 1):
    number = number * 2 - 1
    print(number,"** 2 =", number ** 2)