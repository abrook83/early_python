# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# pword = ''
# for letter in range(1, nr_letters +1):
#     pword += (random.choice(letters))

# for symb in range(1, nr_symbols +1):
#     pword += (random.choice(symbols))

# for num in range(1, nr_numbers +1):
#     pword += (random.choice(numbers))

# print(pword)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


pword_chars = []
for letter in range(1, nr_letters +1):
    pword_chars.append(random.choice(letters))

for symb in range(1, nr_symbols +1):
    pword_chars.append(random.choice(symbols))

for num in range(1, nr_numbers +1):
    pword_chars.append(random.choice(numbers))

random.shuffle(pword_chars)
pword = ""
for char in pword_chars:
    pword += char

print(f"Shhh, your new password is: {pword}")