from math import floor
from time import sleep


def print_zzz(statement):
    print(statement)
    sleep(0.5)


class CoffeeMachine:

    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        },
    }

    COIN_VALUES = {"quarters": 0.25, "dimes": 0.1, "nickels": 0.05, "pennies": 0.01}

    def __init__(self) -> None:
        self.resources = {
            "water": 3000,
            "milk": 1500,
            "coffee": 2500,
            "quarters": 0,
            "dimes": 10,
            "nickels": 10,
            "pennies": 10,
        }

    def report(self):
        print("Current resources:")
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.calc_money_held()}")

    def restock(self):
        self.resources = {
            "water": 3000,
            "milk": 1500,
            "coffee": 2500,
            "quarters": 0,
            "dimes": 10,
            "nickels": 10,
            "pennies": 10,
        }
        self.report()

    def calc_money_held(self):
        money_held = 0
        for coin, value in self.COIN_VALUES.items():
            money_held += self.resources[coin] * value
        return money_held

    def give_change(self, change_required):
        change_total = 0

        def coins_required(coin, change_total):
            value = self.COIN_VALUES[coin]
            coins_required = floor((change_required - change_total) / value)
            if coins_required <= self.resources[coin]:
                change_total += coins_required * value
                self.resources[coin] -= coins_required
            else:
                change_total += self.resources[coin] * value
                self.resources[coin] = 0
            return change_total

        for coin in self.COIN_VALUES:
            change_total = coins_required(coin, change_total)
        return change_total

    def run_machine(self):
        while True:
            choice = input(
                "What would you like? (espresso/latte/cappuccino):\n"
            ).lower()
            if choice == "off":
                break
            elif choice == "report":
                self.report()
            elif choice in self.MENU:
                if self.check_resources(choice):
                    if self.ask_for_money(choice):
                        self.make_coffee(choice)
            else:
                print_zzz("Invalid selection")
        print("Goodbye!")

    def check_resources(self, choice):
        for resource, volume in self.MENU[choice]["ingredients"].items():
            if self.resources[resource] < volume:
                print_zzz(
                    f"Sorry, we don't have enough {resource}. Please choose another option."
                )
                return False
        return True

    def ask_for_money(self, choice):
        money_required = self.MENU[choice]["cost"]
        print_zzz(f"{choice.title()} costs ${money_required}. Please insert coins.")
        coins_given = {
            "quarters": int(input("How many quarters?: ") or "0"),
            "dimes": int(input("How many dimes?: ") or "0"),
            "nickels": int(input("How many nickels?: ") or "0"),
            "pennies": int(input("How many pennies?: ") or "0"),
        }
        money_given = 0
        for coin, number in coins_given.items():
            value = self.COIN_VALUES[coin]
            money_given += number * value
        if money_given < money_required:
            print_zzz(f"You've only given {money_given}, which is not enough.")
            print(f"Money refunded, please start again.")
            return False
        else:
            for coin, number in coins_given.items():
                self.resources[coin] += number
            change_required = money_given - money_required
            change_available = self.give_change(change_required)
            if round(change_available, 2) < round(change_required, 2):
                print_zzz(
                    f"Only ${change_available} out of {change_required} change is available.\n"
                )
                option = input("Would you like your (drink) or a (refund)?:\n")
                if option == "refund":
                    for coin, number in coins_given.items():
                        self.resources[coin] -= number
                    print_zzz("Refund given")
                    return False
            if change_available > 0:
                print_zzz(f"Thank you. Here is ${change_available} change.")
            else:
                print_zzz(f"Thank you. No change required.")
            return True

    def make_coffee(self, choice):
        print_zzz("Thank you for your order.")
        for resource, volume in self.MENU[choice]["ingredients"].items():
            print(f"Adding {resource}.")
            self.resources[resource] -= volume
        print_zzz("Mixing")
        print_zzz(f"Thank you. Here is your {choice}. Enjoy!")


if __name__ == "__main__":
    machine = CoffeeMachine()
    machine.run_machine()
