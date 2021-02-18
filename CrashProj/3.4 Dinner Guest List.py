# DINNER GUESTS
invs = ['christine', 'mum', 'dad']
for peeps in invs:
    print(f"Hey {peeps.title()}, dinner at my joint tomorrow if you're keen!")
unable = invs.pop(1)
decl = f"\nOh no, {unable.title()} can't make it!"
print(decl)
invs.insert(1, 'jared')
print("\nI've found a bigger table though!\n")
invs.insert(0, 'ashley')
invs.insert(1, 'michelle')
invs.append('oli')
for peeps in invs:
    print(f"Hey {peeps.title()}, dinner at my joint tomorrow if you're keen!")

print("\nAh bollocks, table's not gunna be here in time. Can only invite 2!\n")
while len(invs) > 2:
    too_many = invs.pop()
    oust = f"Sorry {too_many.title()}, you're out!"
    print(oust)

print(f"\nNow only {len(invs)} are coming\n")
for rems in invs:
    print(f"Hey {rems.title()}, you can still come!")

del invs[:]
print(f"Names left on the list:{invs}!")