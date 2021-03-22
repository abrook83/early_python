travel_log = [
    {
        "country": "Germany", 
        "cities_visited": ["Berlin","Hamburg","Mannheim","Munich"], 
        "total_visits": 5
    },
    {
        "country": "Netherlands", 
        "cities_visited": ["Amsterdam","Haarlem","Rotterdam","Eindhoven"], 
        "total_visits": 4},
]

#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, cities_visited, visit_count):
    new_country = {}
    new_country["country"] = country
    new_country["cities_visited"] = cities_visited
    new_country["total_visits"] = visit_count
    travel_log.append(new_country)

#🚨 Do not change the code below
add_new_country(country="Russia", visit_count=2, cities_visited=["Moscow", "Saint Petersburg"])
print(travel_log)



