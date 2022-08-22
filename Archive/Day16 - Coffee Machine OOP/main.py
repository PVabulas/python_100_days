from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()


def run_machine():
    items = []
    for item in menu.menu:
        items.append(item.name)
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino):\n").lower()
        if choice == "off":
            break
        elif choice == "report":
            coffee.report()
            money.report()
        elif choice in items:
            drink = menu.menu[items.index(choice)]
            if coffee.is_resource_sufficient(drink):
                if money.make_payment(drink.cost):
                    coffee.make_coffee(drink)
            else:
                print("Insufficient resources, please choose again.")
        else:
            print("Invalid selection")
    print("Goodbye!")


if __name__ == "__main__":
    run_machine()
