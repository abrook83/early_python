from day10_calculatorart import logo
print(logo)

# add
def add(n1, n2):
    return n1 + n2

# subtract
def subtract(n1, n2):
    return n1 - n2

# multiply
def multiply(n1, n2):
    return n1 * n2

# divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

num1 = int(input("What is the first number?:\n"))
for function in operations:
    print(function)
func = input("Select an operation from the above:\n")
num2 = int(input("What is the second number?:\n"))

calc_function = operations[func]        # selects the function from the dict, which uses the defined functions above as its value
answer = calc_function(num1, num2)

print(f"{num1} {func} {num2} = {answer}")