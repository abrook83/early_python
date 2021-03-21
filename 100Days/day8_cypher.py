alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(plain_text, shift_amt):
    encoded = ''
    for i in plain_text:              # for every letter in the text 
        pos = alphabet.index(i)
        new_pos = pos + shift_amt
        encoded += alphabet[new_pos]
    print(f"Encoded text: '{encoded}' ;)")

def decrypt(encoded_text, shift_amt):
    decoded = ''
    for i in encoded_text:
        pos = alphabet.index(i)
        new_pos = pos - shift_amt
        decoded += alphabet[new_pos]
    print(f"Decoded text: '{decoded}'")

if direction == 'e':
    encrypt(plain_text=text, shift_amt=shift)
elif direction == 'd':
    decrypt(encoded_text=text, shift_amt=shift)
