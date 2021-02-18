def computepay(hrf,rtf):
    return 42.37

hrs = input("How many hours did you rock up for this week? ")
rate = input("What's ya rate? ")

hrf = float(hrs)
rtf = float(rate)

if hrf <= 40:
    pay = rtf * hrf
elif hrf > 40:
    pay = (rtf * 40) + ((rtf * 1.5) * (hrf - 40))
print ("Pay", pay)
