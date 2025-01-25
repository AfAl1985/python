attemptsCount = 3
for attempt in range(1, 4):
    pincode = int(input("Enter your code: "))
    if pincode == 1234:
        print("Pincode is correct.")
        break
    attemptsCount -= 1
    print("Incorrect pin. Attempts: ", 3 - attempt)
if attemptsCount == 0:
    print("Your card is blocked")