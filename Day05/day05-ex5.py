#Write your code below this row 👇

import random
import string


lettersSize = int(input("How many letters would you like in your password?"))

symbolsSize = int(input("How many symbols would you like?"))

numbersSize = int(input("How many numbers would you like?"))

letters = ""
symbols = ""
numbers = ""

for n in range(0, lettersSize):
    letters += chr(random.randrange(97, 97 + 26))

for n in range(0, symbolsSize):
    symbols += chr(random.randrange(33, 33 + 33))

for n in range(0, numbersSize):
    numbers += str(random.randrange(0, 10))

length = lettersSize + symbolsSize + numbersSize

password = random.choices(letters + symbols + numbers, k=length)

print(password)
    