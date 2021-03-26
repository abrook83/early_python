## Debug Odd or Even

# # Instructions

# - Read this the code in main.py 
# - Spot the problems 🐞. 
# - Modify the code to fix the program. 

# Fix the code so that it works and passes the tests when you submit. 

# # Hint

# 1. Review the previous lesson and go through the 10 steps to tackle these debugging problems.

# # Solution

# [https://repl.it/@appbrewery/day-13-1-solution](https://repl.it/@appbrewery/day-13-1-solution)

# number = int(input("Which number do you want to check?"))

# if number % 2 == 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")

# year = int(input("Which year do you want to check? "))

# if year % 400 == 0:
#     print("Leap year.")
# elif year % 100 == 0:
#     print("Not leap year.")
# elif year % 4 == 0:
#     print("Leap year.")
# else:
#     print("Not leap year.")

## Debug FizzBuzz

# # Instructions

# - Read this the code in main.py
# - Spot the problems 🐞. 
# - Modify the code to fix the program. 
# - No shortcuts  - don't copy-paste to replace the code entirely with a working solution. 

# The code needs to print the solution to the FizzBuzz game. 

# > `Your program should print each number from 1 to 100 in turn.` 

# >   `When the number is divisible by 3 then instead of printing the number it should print "Fizz".` 

# >     `When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 

# >       `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`

# # Hint

# There is more than one fix required.

# # Solution

# [https://repl.it/@appbrewery/day-13-3-solution](https://repl.it/@appbrewery/day-13-3-solution)

# for number in range(1, 101):
#   if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
#   elif number % 3 == 0:
#     print("Fizz")
#   elif number % 5 == 0:
#     print("Buzz")
#   else:
#     print(number)