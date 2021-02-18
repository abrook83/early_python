x = input("What score did ya get? ")
try:
    xf = float(x)
except:
    print('Please enter a numerical value')
if xf > 1.0:
    print('Invalid score')
    quit()
elif xf >= 0.9:
    print('A')
elif xf >= 0.8:
    print('B')
elif xf >= 0.7:
    print('C')
elif xf >= 0.6:
    print('D')
elif xf < 0.6:
    print('F')
