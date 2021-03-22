alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from day8_art import logo
print(logo)

def ceasar(plain_text, shift_amt, cipher_direction):
    result = ''
    if cipher_direction == 'd':
        shift_amt *= -1
    for i in plain_text:              # for every letter in the text 
        if i in alphabet:
            pos = alphabet.index(i)
            new_pos = pos + shift_amt
            result += alphabet[new_pos]
        else:
            result += i
    print(f"New text: '{result}' ;)")
    
run = True

while run:
    direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26

    ceasar(plain_text=text, shift_amt=shift, cipher_direction=direction)

    again = input("Go again? (y/n):\n")
    if again == 'n':
        run = False
        print("Thanks for comin'!")
