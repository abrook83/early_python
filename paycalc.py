hrs = input("How many hours did you rock up for this week? ")
rate = input("What's ya rate? ")
try:
    hrf = float(hrs)
    rtf = float(rate)
except:
    print("Try again brus, put only numbers in ay!")
    quit()
if hrf <= 40:
    pay = rtf * hrf
elif hrf > 40:
    pay = (rtf * 40) + ((rtf * 1.5) * (hrf - 40))
print ("Coin:", pay)
if pay > 400:
    print("You beauty!")
elif pay > 300:
    print("Not behd, good soize")
else:
    print("Better luck next week")
