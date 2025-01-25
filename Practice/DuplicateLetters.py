string = input("Enter the string: ")
prevSym = ''
equalSym = False
for letter in string:
    if prevSym == letter:
        equalSym = True
        break
    else:
        prevSym = letter

if equalSym:
    print("There are two duplicate letters in a raw")
else:
    print("There aren't duplicat letters here")