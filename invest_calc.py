capit = input("Enter starting amount: ")
fcap = float(capit)

intr = input("Enter interest rate: ")
fint = float(intr)/100

years = input("Term: ")
yrs = float(years)
print(f"Starting amount: {fcap}")
print(f"Interest rate: {fint}")
print(f"Years invested: {yrs}")

count = 1
while count <= yrs:
    acr_int = fcap * fint
    fcap += acr_int
    print(f"Year {count}: {fcap}")
    count += 1
