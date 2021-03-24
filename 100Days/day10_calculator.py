from day10_calculatorart import logo

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

def calculator():
    print(logo)
    num1 = float(input("What is the first number?:\n"))
    for function in operations:
        print(function)
    should_continue = True

    while should_continue:
        func = input("Select an operation:\n")
        num2 = float(input("What is the next number?:\n"))

        calc_function = operations[func]        # selects the function from the dict, which uses the defined functions above as its value
        answer = calc_function(num1, num2)

        print(f"{num1} {func} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}: ") == 'y':
            num1= answer
        else:
            should_continue = False
            calculator()

calculator()