print("Task 7: пропавшая карточка")
# Для настольной игры используются карточки с номерами от 1 до N.
# Одна карточка потерялась. Напишите программу, которая поможет найти потерянную карточку,
# если номера оставшихся известны. Найдите её, зная номера оставшихся карточек.
# Введите число карточек — N.
# Затем введите N − 1 номера оставшихся карточек. Они могут быть введены в любом порядке.

cards = int(input("Enter a quantity of cards: "))
summ = 0
remain_sum = 0

for card in range(1, cards + 1):
    summ += card
for card in range(cards - 1):
    remain_card = int(input("Number a remaining card: "))
    remain_sum += remain_card
total = summ - remain_sum
print(total)
