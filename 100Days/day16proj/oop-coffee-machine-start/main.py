from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# menu = Menu()
# menu_item = MenuItem()

money_machine = MoneyMachine()      # assigns the class to the variable
coffee_maker = CoffeeMaker()
menu = Menu()

money_machine.report()              # call the 'report' function from the class
coffee_maker.report()

machine_avail = True

while machine_avail:
    options = menu.get_items()
    request = input("What would you like? (espresso, latte or capuccino):\n").lower()
    if request == 'off':
        print("Seeya later!")
        machine_avail = False
    elif request == 'report':
        coffee_maker.report()
        money_machine .report()
    else:
        drink = menu.find_drink(request)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)