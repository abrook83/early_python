import random

while True:
    go = input('Ready? (y/n): ')
    if go == 'n':
        break
    elif go == 'y':
        roll = random.randint(1,6)
        print(roll)
