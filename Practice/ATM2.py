while True:
    for attempt in range(1, 4):
        pincode = int(input("Enter your code: "))
        if pincode == 1234:
            print("\nPincode is correct.")
            break
        print("Incorrect pin. Attempts: ", 3 - attempt)
    else:
        print("\nYour card is blocked")
    print("Next client please!")