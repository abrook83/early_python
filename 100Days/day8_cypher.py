import math

# def greet_with_name(name, when):
#     print(f"G'day {name}!")
#     print(f"How ya goin' {when} {name}?")
#     print(f"Watcha doin' {when} {name}?")

# greet_with_name(when = 'today', name = "Big Dogg",)

## Area Calc

test_h = int(input("What is the wall's height?\n"))
test_w = int(input("What is the wall's width?\n"))

def calculate_cans(w,h,cover):
    wall_area = int(w) * int(h)
    print(f"\nYou'll need {math.ceil(wall_area / cover)} cans of paint.\n")      # math.ciel rounds up!!

calculate_cans(test_w,test_h, 5)