valid = False
while not valid:
    try:
        cost = float(input("How much was your meal? "))
        if cost > 0:
            valid = True
    except:
        print("please enter a valid amount.")

valid = False
while not valid:
    try:
        percent = float(input("What percent tip would you like to leave? "))
        valid = True
    except:
        print("please enter a valid amount.")

print("your tip should be $" + str(f'{cost*percent*.01:.2f}') + " for a total of $" + str(f'{cost+cost*percent*.01:.2f}'))