totalHours = int(input("Enter a number of hours: "))
cells = 1

for hour in range(1, totalHours + 1):
    cells *= 2
    print("Passed ours: ", hour)
    print("A number of cells: ", cells)
    print("Hours left: ", totalHours - hour)
    print()
print("Observing finished!")