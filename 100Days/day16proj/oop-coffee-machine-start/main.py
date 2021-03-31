from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine
coffee_maker = CoffeeMaker
menu = Menu
menu_item = MenuItem

machine_avail = True

while machine_avail:
    request = input("What would you like? (espresso, latte or capuccino):\n").lower()
    if request == 'off':
        print("Seeya later!")
        machine_avail = False
    elif request == 'report':
        coffee_maker.report()
        money_machine.report()
    else:               
        menu.find_drink(request)                        # take the coffee type input, take its ingredients from the MENU, label that as 'drink_type'...
        if CoffeeMaker.is_resource_sufficient(request):      # load the ingredients list into the 'check_resources', return a T or F
            to_pay = count_coins()                          # get the total amount paid from 'count_coins'
            if paid(to_pay, drink_type['cost']):            # if paid amount > price...
                make_coffee(request, drink_type["ingredients"])     # make the desired coffee from the input, and its retrieved ingredients

