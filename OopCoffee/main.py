from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import art

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

print(art.cup)
print(art.logo)

while is_on:
    options = menu.get_items()
    preferences = input(f"What would you like? ({options}): ").lower()
    if preferences == "off":
        is_on = False
        print("Turning off the machine.")
    elif preferences == "report":
        coffee_maker.report()
        money_machine.report()
    elif preferences == "refill":
        coffee_maker.refill_resources()
    else:
        drink = menu.find_drink(preferences)
        if drink is not None:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)