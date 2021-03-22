programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    }
print(programming_dictionary["Function"])

# add a value
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

# create empty dict
empty_dictionary = {}

# wipe a dicitonary
# programming_dictionary = {}
# print(programming_dictionary)

programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# loop through
for thing in programming_dictionary:
    print(f"{thing}:")
    print(programming_dictionary[thing])

# nesting
travel_log = {
    "Germany": {"cities_visited": ["Berlin","Hamburg","Mannheim","Munich"], "total_visits": 5},
    "Netherlands": {"cities_visited": ["Amsterdam","Haarlem","Rotterdam","Eindhoven"], "total_visits": 4},
}

travel_list = [
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