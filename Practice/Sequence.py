seqNum = int(input("Enter a number of digits: "))
numeral = int(input("What digit do you prefer? "))
while numeral < 0 or numeral > 9:
    numeral = int(input('digit i sout of range. Enter a new one: '))
numeralCount = 0
for num in range(seqNum):
    print("Enter", num, "number: ", end= '')
    number = int(input())
    while number > 0:
        if number % 10 == numeral:
            numeralCount+= 1
        number //= 10
print("A number of digits", numeral, "In sequence: ", numeralCount)