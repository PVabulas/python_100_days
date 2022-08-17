import os
import art


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def ask_for_bid():
    cls()
    print(art.logo)
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: £"))
    return name, bid


def run_auction():
    input("Welcome to the auction, when ready press Enter:")
    bids = {}
    while True:
        name, bid = ask_for_bid()
        bids[name] = bid
        if input("Is there another bid, Y/N?: ") == "N":
            break
    highest_bid = 0
    for name, bid in bids.items():
        if bid > highest_bid:
            highest_bidder = name
            highest_bid = bid
    print(
        f"Thank you. The winner of the auction is {highest_bidder}, with a bid of £{highest_bid}."
    )


def run_auction_house():
    print(art.logo)
    print("Welcome to the Auction House.")
    while True:
        run_auction()
        if input("Is there another auction, Y/N?: ") == "N":
            break


run_auction_house()
