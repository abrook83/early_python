alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def ceasar(plain_text, shift_amt, cipher_direction):
    result = ''
    if cipher_direction == 'd':
        shift_amt *= -1
    for i in plain_text:              # for every letter in the text 
        pos = alphabet.index(i)
        new_pos = pos + shift_amt
        result += alphabet[new_pos]
    print(f"New text: '{result}' ;)")

ceasar(plain_text=text, shift_amt=shift, cipher_direction=direction)
