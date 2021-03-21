import math

# def greet_with_name(name, when):
#     print(f"G'day {name}!")
#     print(f"How ya goin' {when} {name}?")
#     print(f"Watcha doin' {when} {name}?")

# greet_with_name(when = 'today', name = "Big Dogg",)

### Required paint cans calculator ###

# test_h = int(input("What is the wall's height?\n"))
# test_w = int(input("What is the wall's width?\n"))

# def calculate_cans(w,h,cover):
#     wall_area = int(w) * int(h)
#     print(f"\nYou'll need {math.ceil(wall_area / cover)} cans of paint.\n")      # math.ciel rounds up!!

# calculate_cans(test_w,test_h, 5)

### check for prime numbers ###

# num = int(input("Enter a number between 1 & 100:\n"))

# def prime_check(num):
#     is_prime = True
#     for i in range(2,num):
#         if num % i == 0:
#             is_prime = False
#     if is_prime:
#         print(f"{num} is a prime number")
#     else:
#         print(f"Nope, {num} is not a prime number")

# prime_check(num)