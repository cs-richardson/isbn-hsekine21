'''
Prompts the user for a number and checks if it is an ISBN number 
Hina Sekine
'''
# Program initialization
import math
numLength = 10

# user input 
isbn = input("ISBN: ")
while isbn.isdigit() == False or len(isbn) != numLength:
    isbn = input("Retry: ")
isbn = int(isbn)

# last digit 
lastDigit = isbn % 10

# multiplies the 1st to 9th digit by their index (starting at 1) and adds them
calcNum = 0
for i in range(numLength, 1, -1):
    digit = ((isbn % (10 ** i)) - (isbn % (10 ** (i - 1)))) / (10 ** (i - 1))
    calcNum = calcNum + (digit * (abs(i - numLength) + 1))
    x
# mod by 11 
final = calcNum % 11

# output 
if final == lastDigit:
    print("YES")
else:
    print("NO")
