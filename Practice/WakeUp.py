wake_up = int(input("Awaking time: "))
water = 0
calories_sum = 0

for hour in range(wake_up, 23, 3):
    water += 1
    print("Time to have a meal", hour, "hours")
    calories = int(input("How much did you eat? "))
    calories_sum += calories
print("Drunk liters of water: ", water)
print("Calories: ", calories_sum)