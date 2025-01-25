people = int(input("Enter a number of people: "))
for hour in range(people + 1):
    print("An hour is passing: ", hour)
    for num in range(hour, people):
        print("Enter a number in queye: ", num)
    print()
print("The is off!")