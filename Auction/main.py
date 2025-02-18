from gavel import gavel
import os
print("\n" * 2)
print("Welcome to the Secret Auction Program!")
print(f"\033[35m{gavel}\033[0m")

run = True
while run:
    bids = {}
    name = input("\033[0mWhat is your name: \033[35m")
    bid = int(input("\033[0mWhat is your bid: \033[35m$"))
    bids[name] = bid
    more_bids = input("\033[0mAre there any more bids? Type 'yes' or 'no': \033[35m")
    if more_bids == "yes":
        os.system("clear")
        continue
    if more_bids == "no":
        highest_bid = max(bids.values())
        for key, value in bids.items():
            if value == highest_bid:
                winner = key
        print(f"\033[0mThe winner is \033[35m{winner}\033[0m with a bid of \033[35m${highest_bid}\033[0m")
        run_again = input("Would you like to run the auction again? Type 'yes' or 'no': \033[35m")
        if run_again == "no":
            run = False
            print(" 👋 Goodbye, Have a Nice Day! 👋")
        else:
            os.system("clear")
            continue
        