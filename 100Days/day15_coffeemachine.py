from day15_menu import MENU, resources
# print(MENU)
# print(resources)
# TODO 1 "What would you like?" - either coffees, report or OFF function. Afterward, show prompt again to await next direction...

ingredients_avail = True
       
def make_coffee():
    request = input("What would you like? (espresso, latte or capuccino):\n")
    # for coffee_type, ingredient in MENU.items():
    print(f"\nMaking 1 * {request}\n")
    water = int(MENU[request]['ingredients']['water'])
    resources['water'] -= water
    print(f"Water req. - {water}ml")
    # print(f"Water left - {resources['water']}")
    coffee = int(MENU[request]['ingredients']['coffee'])
    resources['coffee'] -= coffee    
    print(f"Coffee req. - {coffee}g")
    # print(f"Coffee left - {resources['coffee']}")
    milk = int(MENU[request]['ingredients']['milk'])
    resources['milk'] -= milk    
    print(f"Milk req. - {milk}ml")          # what to do for espresso as it uses no milk
    # print(f"Milk left - {resources['milk']}")


if resources['milk'] <= 0:
    ingredients_avail = False
elif resources['water'] <= 0:
    ingredients_avail = False
elif resources['coffee'] <= 0:  
    ingredients_avail = False


while ingredients_avail == True:
    make_coffee()

# TODO check for sufficient resources to make a drink, feedback to user if not available



# TODO count coins by the quantity of each coin, calculate the total money input

def count_coins():
    total_in = float(input("How many quarters?: ")) * 0.25
    total_in += float(input("How many dimes?: ")) * 0.1
    total_in += float(input("How many nickels?: ")) * 0.05
    total_in += int(input("How many pennies?: ")) * 0.01
    return total_in

# TODO calculate change... Determine if transaction successful.

def enough(coffee_price, coins_input):          # generate these variables to enter into the function...
    if coins_input > coffee_price:
        enough = True
        print(f"Change: ${float(coins_input - coffee_price)}")
    else:
        enough = False
        print("Sorry, you haven't put in enough money...")

# make coffee, reduct resources from the available in the machine.


