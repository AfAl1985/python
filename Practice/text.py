text = input("Enter the text: ")
first_sym = input("Enter the first letter: ")
second_sym = input("Enter the second letter: ")
firstSymCount = 0
secondSymCount = 0

for symbol in text:
    if symbol == first_sym:
        firstSymCount += 1
    if symbol == second_sym:
        secondSymCount += 1

print("A number of letters ", first_sym, "=", firstSymCount)
print("A number of letters ", second_sym, "=", secondSymCount)