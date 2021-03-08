# CITIES
cities = ['berlin', 'hamburg', 'cologne', 'bonn', 'frankfurt']
live = f"We're moving to {cities[0].title()}"
print(live)
cities.insert(1, 'leipzig')
live = f"...or maybe we'll go to {cities[-2].title()} instead!"
print(live)
pop_cit = cities.pop()
live = f"Actually, fuck it, let's go to {cities[-2].title()}!"
print(live)
print(f"we're definitely not moving to {pop_cit.title()}!")