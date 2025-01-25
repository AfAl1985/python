badGradeCount = 0
for student in range(5):
    answer = input("Who is the author? ")
    if (answer == 'Pushkin') or (answer == 'pushkin'):
        print("That's right")
        break
    print("Wrong!")
    badGradeCount += 1
print("A number of bad marks: ", badGradeCount)