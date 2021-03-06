from day15_menu import MENU, resources

# TODO make coffee, deduct resources from the available in the machine.


def make_coffee(coffee_type, ingredients):
    """Makes the desired coffee from the user input, deducting the resources from the available"""
    print(f"\nMaking 1 * {coffee_type}\n")
    for item in ingredients:      # for each item in the imput ingredients list
        resources[item] -= ingredients[item]       # take the resource amount of the item away from the total resources


# TODO generate a report when requested


def gen_report():
    """Reports the available resources in the machine"""
    print("Resources available:")           # hold 'alt + shift' to select multipl lines, WHOA!!!
    print(f"Water - {resources['water']}ml")
    print(f"Coffee - {resources['coffee']}g")
    print(f"Milk - {resources['milk']}ml")


# TODO check for sufficient resources to make a drink, feedback to user if not available


def check_resources(ingredients):       # loads in the ingredients list from the MENU item
    """Checks if the requested ingredient is more than is available"""
    for item in ingredients:            # for each item in that ingredients list...
        if ingredients[item] > resources[item]:         # if there's more of the ingredient than there is available...
            print(f"Sorry, we're out of {item}!")       # sorry, we're out
            return False            # check_resources = False
    return True         # or else check_resources is True


# TODO count coins by the quantity of each coin, calculate the total money input


def count_coins():
    """Counts the total of the coins input into the machine"""
    total_in = float(input("How many quarters?: ")) * 0.25
    total_in += float(input("How many dimes?: ")) * 0.1
    total_in += float(input("How many nickels?: ")) * 0.05
    total_in += int(input("How many pennies?: ")) * 0.01
    return total_in


# # TODO calculate change... Determine if transaction successful.


def paid(paid_amount, price):
    """Ensures the paid amount is more than the price, calculates change due"""
    if paid_amount > price:
        change_due = paid_amount - price
        print(f"Change: ${change_due:.2f}")     # rounds the change to 2 decimal places
        return True
    else:
        print("Sorry, that's not enough...")
        return False


# TODO 1 "What would you like?" - either coffees, report or OFF function. Afterward, show prompt again to await next direction...


machine_avail = True

while machine_avail:
    request = input("What would you like? (espresso, latte or capuccino):\n").lower()
    if request == 'off':
        print("Seeya later!")
        machine_avail = False
    elif request == 'report':
        gen_report()        # generate the report of available resources
    else:               
        drink_type = MENU[request]      # take the coffee type input, take its ingredients from the MENU, label that as 'drink_type'...
        if check_resources(drink_type["ingredients"]):      # load the ingredients list into the 'check_resources', return a T or F
            to_pay = count_coins()                          # get the total amount paid from 'count_coins'
            if paid(to_pay, drink_type['cost']):            # if paid amount > price...
                make_coffee(request, drink_type["ingredients"])     # make the desired coffee from the input, and its retrieved ingredients


#### early workings..... #####


# if resources['milk'] <= 0:
#     ingredients_avail = False
# elif resources['water'] <= 0:
#     ingredients_avail = False
# elif resources['coffee'] <= 0:  
#     ingredients_avail = False


# while ingredients_avail == True:
#     make_coffee()



# # def check_resources(coffee_price, coins_input):          # generate these variables to enter into the function...
# #     if coins_input > coffee_price:
# #         enough = True
# #         print(f"Change: ${float(coins_input - coffee_price)}")
# #     else:
# #         enough = False
# #         print("Sorry, you haven't put in enough money...")



