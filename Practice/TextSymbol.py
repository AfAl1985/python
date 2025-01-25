text = input("Enter the text: ")
summ = 0
print('\nFiltered text:', end= ' ')
for symbol in text:
    if symbol == '1' or symbol == '9':
        summ += int(symbol)
    else:
        print(symbol, end= '')
print('\nSum: ', summ)