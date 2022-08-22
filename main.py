from menu import Menu
from menu import MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
drink2order = Menu()
prompt = drink2order.get_items()
cha_ching = MoneyMachine()


def prompt_user():
    user_choice = input(f"What would you like? {prompt}:\n")
    return user_choice


def coffee_machine():
    user_choice = prompt_user()
    if user_choice.lower() == "off":
        print("Shutting down")
        return 0
    elif user_choice.lower() == 'report':
        coffee_maker.report()
        cha_ching.report()
        return 1
    elif user_choice.lower() in prompt:
        drink = drink2order.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) and cha_ching.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
            return 1
        else:
            return 0


power_switch = True
#
while power_switch:
    power_switch = coffee_machine()
