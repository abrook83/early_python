from day15_menu import MENU, resources
# print(MENU)
# print(resources)
# TODO 1 "What would you like?" - either coffees, report or OFF function. Afterward, show prompt again to await next direction...

def make_coffee():
    request = input("What would you like? (espresso, latte or capuccino):\n")
    for coffee_type, ingredient in MENU.items():
        print(f"Making 1 * {coffee_type}")
        water = MENU[coffee_type]['ingredients']['water']
        print(f"Water req. {water}ml")
        coffee = MENU[coffee_type]['ingredients']['coffee']
        print(f"Coffee req {coffee}g")
        milk = MENU[coffee_type]['ingredients']['milk']
        print(f"Milk req. {milk}ml")

make_coffee()

# TODO check for sufficient resources to make a drink, feedback to user if not available



# TODO count coins by the quantity of each coin, calculate money input

def count_coins():
    quarters_in = float(input("How many quarters?: ")) * 0.25
    dimes_in = float(input("How many dimes?: ")) * 0.1
    nickels_in = float(input("How many nickels?: ")) * 0.05
    pennies_in = int(input("How many pennies?: ")) * 0.01
    total_in = (quarters_in + dimes_in + nickels_in + pennies_in)
    print(f"\nTotal coins in: ${total_in}")

# TODO calculate change... Determine if transaction successful.

def enough(coffee_price, coins_input):          # generate these variables to enter into the function...
    if coins_input > coffee_price:
        enough = True
        print(f"Change: ${float(coins_input - coffee_price)}")
    else:
        enough = False
        print("Sorry, you haven't put in enough money...")

# make coffee, reduct resources from the available in the machine.
