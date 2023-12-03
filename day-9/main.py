from art import gavel
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

bidders = {}

print(gavel)
print("Welcome to the blind auction")

auction = True

while(auction):
    name = input("What is your name? ")
    bid = input("What is your bid? ")
    while(bid.isnumeric() is False):
        print('numbers only please')
        bid = input("What is your bid? ")

    bid = int(bid)
    bidders[name] = bid

    again = ''
    while again != 'y' and again != 'n':
        again = input("Are there any other bidders? (yes/no) ")[0].lower()
        if again != 'y' and again != 'n':
            print('Please only type yes or no')
    
    clear()

    if again == 'n':
        auction = False

winner = ''
max = 0
for bidder in bidders:
    if bidders[bidder] > max:
        winner = bidder
        max = bidders[bidder]

print('The winner is ' + (winner) + ' with a bid of $' + str(max))