from main_logo import logo
from os import system

print(logo)
print("___<Welcome to the secret auction program>___\n")
auction_dict = {}


def dictionary_adder(name, bid):
    auction_dict[name] = bid


def dictionary_printer():
    max_bid = 0 # Try to use function 'max' instead 'for'
    for key in auction_dict:
        if auction_dict[key] > max_bid:
            max_bid = auction_dict[key]
            max_user = key
    print(f"The winner is {max_user} with a bid of ${max_bid}")


while True:
    user_name = input("What is your name? -> ")
    user_bid = int(input("What's your bid? -> $"))
    # There will be def function with algorithm
    dictionary_adder(user_name, user_bid)
    other_user = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other_user == "yes" or other_user == "y":
        system('cls||clear')
        continue
    else:
        break
system('cls||clear')
dictionary_printer()