capit = input("Enter starting amount: ")
fcap = float(capit)

intr = input("Enter interest rate in percentage: ")
fint = float(intr)/100

years = input("Term: ")
yrs = float(years)

print(f"\nStarting amount: ${capit}")
print(f"Interest rate: {intr}%")
print(f"Years invested: {int(yrs)}")

count = 1
while count <= yrs:
    acr_int = fcap * fint
    fcap += acr_int
    print(f"Year {count}: {fcap}")
    count += 1
