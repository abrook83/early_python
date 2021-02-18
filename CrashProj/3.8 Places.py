# SEE THE WORLD
places = ['petra', 'kruger', 'russia', 'algeria', 'mozambique']
print("\nSorted:")
print (sorted(places))

print("\nOriginal:")
print(places)

print("\nReverse Sorted:")
print(sorted(places, reverse=True))

print("\nOriginal:")
print(places)

print("\nReverse permanently:")
places.reverse()
print(places)

print("\nFlip 'im back:")
places.reverse()
print(places)

print("\nSort permanently:")
places.sort()
print(places)

print("\nReversed & Sorted:")
places.sort(reverse=True)
print(places)
